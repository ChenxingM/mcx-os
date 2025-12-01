; ===========================================
; boot.asm - 主引导程序
; ===========================================

[bits 16]
[org 0x7c00]

KERNEL_OFFSET equ 0x1000    ; 内核加载到这个地址

start:
    ; 设置段寄存器(　レジスターの設定　)
    xor ax, ax
    mov ds, ax
    mov es, ax
    mov ss, ax
    mov sp, 0x9000          ; 栈顶

    mov [BOOT_DRIVE], dl    ; BIOS 把启动驱动器号放在 dl

    ; 打印启动消息
    mov si, MSG_BOOT
    call print_string

    ; 加载内核
    mov si, MSG_LOAD
    call print_string

    mov bx, KERNEL_OFFSET   ; 读到哪
    mov dh, 15              ; 读多少扇区
    mov dl, [BOOT_DRIVE]    ; 从哪个驱动器
    call disk_load

    ; 切换到保护模式
    mov si, MSG_SWITCH
    call print_string

    call switch_to_pm

    jmp $                   ; 不应该到这里

; ---------------------------------------
; 打印字符串函数
; 输入: si = 字符串地址
; ---------------------------------------
print_string:
    push ax
.loop:
    lodsb
    cmp al, 0
    je .done
    mov ah, 0x0e
    int 0x10
    jmp .loop
.done:
    pop ax
    ret

; ---------------------------------------
; 数据
; ---------------------------------------
BOOT_DRIVE:     db 0
MSG_BOOT:       db 'Booting...', 13, 10, 0
MSG_LOAD:       db 'Loading kernel...', 13, 10, 0
MSG_SWITCH:     db 'Switching to protected mode...', 13, 10, 0

; ---------------------------------------
; 包含其他文件
; ---------------------------------------
%include "disk.asm"
%include "gdt.asm"
%include "switch_pm.asm"

; ---------------------------------------
; 填充到 512 字节
; ---------------------------------------
times 510-($-$$) db 0
dw 0xaa55