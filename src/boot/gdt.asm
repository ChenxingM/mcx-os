; ===========================================
; gdt.asm - 全局描述符表
; ===========================================

gdt_start:

; 第一个描述符必须是空的（CPU 规定）
gdt_null:
    dd 0x0
    dd 0x0

; 代码段描述符
gdt_code:
    dw 0xffff       ; 段界限 (bits 0-15)
    dw 0x0          ; 基地址 (bits 0-15)
    db 0x0          ; 基地址 (bits 16-23)
    db 10011010b    ; 访问字节
    db 11001111b    ; 标志 + 段界限 (bits 16-19)
    db 0x0          ; 基地址 (bits 24-31)

; 数据段描述符
gdt_data:
    dw 0xffff
    dw 0x0
    db 0x0
    db 10010010b    ; 访问字节（数据段）
    db 11001111b
    db 0x0

gdt_end:

; GDT 描述符（告诉 CPU GDT 在哪）
gdt_descriptor:
    dw gdt_end - gdt_start - 1    ; 大小
    dd gdt_start                   ; 地址

; 常量：段选择子
CODE_SEG equ gdt_code - gdt_start
DATA_SEG equ gdt_data - gdt_start
