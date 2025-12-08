; ===========================================
; isr.asm - 中断入口点
; ===========================================

[bits 32]

; 导出符号
global idt_load
global isr0, isr1, isr2, isr3, isr4, isr5, isr6, isr7
global isr8, isr9, isr10, isr11, isr12, isr13, isr14, isr15
global isr16, isr17, isr18, isr19, isr20, isr21, isr22, isr23
global isr24, isr25, isr26, isr27, isr28, isr29, isr30, isr31
global irq0, irq1, irq2, irq3, irq4, irq5, irq6, irq7
global irq8, irq9, irq10, irq11, irq12, irq13, irq14, irq15

; 外部 C 函数
extern isr_handler
extern irq_handler

; -------------------------------------------
; 加载 IDT
; -------------------------------------------
idt_load:
    mov eax, [esp + 4]      ; 获取参数（IDT 指针地址）
    lidt [eax]              ; 加载 IDT
    ret

; -------------------------------------------
; 异常处理入口 (0-31)
; 有些异常 CPU 会自动压入错误码，有些不会
; 我们统一格式：没有错误码的手动压入 0
; -------------------------------------------

; 无错误码的异常
%macro ISR_NOERRCODE 1
isr%1:
    push dword 0            ; 压入假的错误码
    push dword %1           ; 压入中断号
    jmp isr_common
%endmacro

; 有错误码的异常
%macro ISR_ERRCODE 1
isr%1:
    push dword %1           ; 压入中断号（错误码 CPU 已经压入）
    jmp isr_common
%endmacro

; 异常 0-31
ISR_NOERRCODE 0     ; 除零
ISR_NOERRCODE 1     ; 调试
ISR_NOERRCODE 2     ; NMI
ISR_NOERRCODE 3     ; 断点
ISR_NOERRCODE 4     ; 溢出
ISR_NOERRCODE 5     ; 越界
ISR_NOERRCODE 6     ; 非法指令
ISR_NOERRCODE 7     ; 无协处理器
ISR_ERRCODE   8     ; 双重故障
ISR_NOERRCODE 9     ; 协处理器段越界
ISR_ERRCODE   10    ; 无效 TSS
ISR_ERRCODE   11    ; 段不存在
ISR_ERRCODE   12    ; 栈段错误
ISR_ERRCODE   13    ; 一般保护故障
ISR_ERRCODE   14    ; 页故障
ISR_NOERRCODE 15    ; 保留
ISR_NOERRCODE 16    ; 浮点错误
ISR_ERRCODE   17    ; 对齐检查
ISR_NOERRCODE 18    ; 机器检查
ISR_NOERRCODE 19    ; SIMD 浮点异常
ISR_NOERRCODE 20
ISR_NOERRCODE 21
ISR_NOERRCODE 22
ISR_NOERRCODE 23
ISR_NOERRCODE 24
ISR_NOERRCODE 25
ISR_NOERRCODE 26
ISR_NOERRCODE 27
ISR_NOERRCODE 28
ISR_NOERRCODE 29
ISR_NOERRCODE 30
ISR_NOERRCODE 31

; -------------------------------------------
; 硬件中断入口 (IRQ 0-15 -> INT 32-47)
; -------------------------------------------
%macro IRQ 2
irq%1:
    push dword 0            ; 无错误码
    push dword %2           ; 压入中断号
    jmp irq_common
%endmacro

IRQ 0,  32      ; 定时器
IRQ 1,  33      ; 键盘
IRQ 2,  34      ; 级联
IRQ 3,  35      ; COM2
IRQ 4,  36      ; COM1
IRQ 5,  37      ; LPT2
IRQ 6,  38      ; 软盘
IRQ 7,  39      ; LPT1
IRQ 8,  40      ; CMOS 时钟
IRQ 9,  41
IRQ 10, 42
IRQ 11, 43
IRQ 12, 44      ; 鼠标
IRQ 13, 45      ; 协处理器
IRQ 14, 46      ; 硬盘
IRQ 15, 47

; -------------------------------------------
; 公共处理部分
; -------------------------------------------
isr_common:
    ; 保存所有寄存器
    pusha                   ; 压入 eax, ecx, edx, ebx, esp, ebp, esi, edi

    ; 保存数据段
    mov ax, ds
    push eax

    ; 切换到内核数据段
    mov ax, 0x10            ; 内核数据段选择子
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    ; 调用 C 处理函数，参数是栈指针
    push esp
    call isr_handler
    add esp, 4

    ; 恢复数据段
    pop eax
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    ; 恢复所有寄存器
    popa

    ; 清除错误码和中断号
    add esp, 8

    ; 返回
    iret

irq_common:
    pusha

    mov ax, ds
    push eax

    mov ax, 0x10
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    push esp
    call irq_handler
    add esp, 4

    pop eax
    mov ds, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    popa
    add esp, 8
    iret