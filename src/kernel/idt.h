#ifndef IDT_H
#define IDT_H

#include <stdint.h>

/* IDT 条目结构（8 字节） */
struct idt_entry {
    uint16_t base_low;      /* 处理程序地址低 16 位 */
    uint16_t selector;      /* 代码段选择子 */
    uint8_t  zero;          /* 保留，必须为 0 */
    uint8_t  flags;         /* 类型和属性 */
    uint16_t base_high;     /* 处理程序地址高 16 位 */
} __attribute__((packed));

/* IDT 指针结构（给 lidt 指令用） */
struct idt_ptr {
    uint16_t limit;         /* IDT 大小 - 1 */
    uint32_t base;          /* IDT 地址 */
} __attribute__((packed));

void idt_init(void);
void idt_set_gate(uint8_t num, uint32_t base, uint16_t selector, uint8_t flags);

#endif