; ===========================================
; disk.asm - 磁盘读取
; ===========================================
; 输入:
;   dh = 要读取的扇区数
;   dl = 驱动器号
;   bx = 读取到的内存地址
; ===========================================

disk_load:
    push dx             ; 保存 dx

    mov ah, 0x02        ; BIOS 功能：读扇区
    mov al, dh          ; 读取扇区数
    mov ch, 0           ; 柱面 0
    mov cl, 2           ; 从第 2 扇区开始
    mov dh, 0           ; 磁头 0

    int 0x13            ; 调用 BIOS

    jc disk_error       ; 如果出错（CF=1），跳转

    pop dx
    cmp al, dh          ; 实际读取数 == 请求数？
    jne disk_error

    ret

disk_error:
    mov si, disk_error_msg
    call print_string
    jmp $

disk_error_msg: db 'Disk read error!', 0