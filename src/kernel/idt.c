/* ===========================================
* idt.c - 中断描述符表
 * =========================================== */

#include "idt.h"
#include "isr.h"

#define IDT_ENTRIES 256

struct idt_entry idt[IDT_ENTRIES];
struct idt_ptr idtp;

/* 汇编函数，加载 IDT */
extern void idt_load(uint32_t);

/* 设置一个 IDT 条目 */
void idt_set_gate(uint8_t num, uint32_t base, uint16_t selector, uint8_t flags) {
    idt[num].base_low  = base & 0xFFFF;
    idt[num].base_high = (base >> 16) & 0xFFFF;
    idt[num].selector  = selector;
    idt[num].zero      = 0;
    idt[num].flags     = flags;
}

/* 初始化 IDT */
void idt_init(void) {
    idtp.limit = sizeof(idt) - 1;
    idtp.base  = (uint32_t)&idt;

    /* 清空 IDT */
    for (int i = 0; i < IDT_ENTRIES; i++) {
        idt_set_gate(i, 0, 0, 0);
    }

    /* 注册中断处理程序（下一步实现） */
    isr_init();

    /* 加载 IDT */
    idt_load((uint32_t)&idtp);
}
