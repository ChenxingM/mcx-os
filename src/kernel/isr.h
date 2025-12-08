#ifndef ISR_H
#define ISR_H

#include <stdint.h>

/* 中断时 CPU 压入栈的寄存器 */
struct interrupt_frame {
    /* 我们压入的寄存器 */
    uint32_t ds;
    uint32_t edi, esi, ebp, esp, ebx, edx, ecx, eax;
    
    /* 中断号和错误码 */
    uint32_t int_no, err_code;
    
    /* CPU 自动压入的 */
    uint32_t eip, cs, eflags, useresp, ss;
};

void isr_init(void);
void isr_handler(struct interrupt_frame *frame);
void irq_handler(struct interrupt_frame *frame);

/* 注册中断回调 */
typedef void (*isr_callback_t)(struct interrupt_frame *);
void register_interrupt_handler(uint8_t n, isr_callback_t handler);

#endif