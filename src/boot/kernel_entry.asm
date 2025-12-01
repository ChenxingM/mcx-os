; ===========================================
; kernel_entry.asm - 内核入口
; ===========================================
; 从汇编跳转到 C 语言的桥梁

[bits 32]
[extern kernel_main]    ; 声明外部的 C 函数

global _start
_start:
    call kernel_main    ; 调用 C 的 kernel_main()
    jmp $               ; 如果返回，无限循环