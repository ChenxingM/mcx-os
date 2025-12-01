; ===========================================
; switch_pm.asm - 切换到 32 位保护模式
; ===========================================

[bits 16]
switch_to_pm:
    cli                     ; 1. 关闭中断（切换过程中不能被打扰）

    lgdt [gdt_descriptor]   ; 2. 加载 GDT

    mov eax, cr0            ; 3. 修改 cr0 寄存器
    or eax, 0x1             ;    把最低位设为 1
    mov cr0, eax            ;    正式开启保护模式！

    jmp CODE_SEG:init_pm    ; 4. 远跳转，清空 CPU 流水线

[bits 32]
init_pm:
    ; 现在是 32 位模式了！

    mov ax, DATA_SEG        ; 5. 更新所有段寄存器
    mov ds, ax
    mov ss, ax
    mov es, ax
    mov fs, ax
    mov gs, ax

    mov ebp, 0x90000        ; 6. 设置栈顶
    mov esp, ebp

    call KERNEL_OFFSET      ; 7. 跳转到内核！

