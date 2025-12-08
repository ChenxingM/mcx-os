/* ===========================================
 * kernel.c - 内核主程序
 * =========================================== */

#include "idt.h"
#include "keyboard.h"

/* VGA 文本模式常量 */
#define VIDEO_MEMORY 0xB8000
#define SCREEN_WIDTH 80
#define SCREEN_HEIGHT 25
#define WHITE_ON_BLACK 0x0F

/* 当前光标位置 */
static int cursor_x = 0;
static int cursor_y = 0;

/* 清屏 */
void clear_screen(void) {
    char *video = (char *)VIDEO_MEMORY;
    int i;
    for (i = 0; i < SCREEN_WIDTH * SCREEN_HEIGHT * 2; i += 2) {
        video[i] = ' ';
        video[i + 1] = WHITE_ON_BLACK;
    }
    cursor_x = 0;
    cursor_y = 0;
}

/* 滚动屏幕 */
static void scroll(void) {
    char *video = (char *)VIDEO_MEMORY;
    int i;

    if (cursor_y >= SCREEN_HEIGHT) {
        /* 把所有行往上移一行 */
        for (i = 0; i < (SCREEN_HEIGHT - 1) * SCREEN_WIDTH * 2; i++) {
            video[i] = video[i + SCREEN_WIDTH * 2];
        }
        /* 清空最后一行 */
        for (i = (SCREEN_HEIGHT - 1) * SCREEN_WIDTH * 2;
             i < SCREEN_HEIGHT * SCREEN_WIDTH * 2; i += 2) {
            video[i] = ' ';
            video[i + 1] = WHITE_ON_BLACK;
        }
        cursor_y = SCREEN_HEIGHT - 1;
    }
}

/* 打印单个字符 */
void print_char(char c) {
    char *video = (char *)VIDEO_MEMORY;

    if (c == '\n') {
        cursor_x = 0;
        cursor_y++;
    } else if (c == '\b') {
        /* 退格 */
        if (cursor_x > 0) {
            cursor_x--;
            int offset = (cursor_y * SCREEN_WIDTH + cursor_x) * 2;
            video[offset] = ' ';
            video[offset + 1] = WHITE_ON_BLACK;
        }
    } else if (c == '\t') {
        /* Tab：移动到下一个 4 的倍数 */
        cursor_x = (cursor_x + 4) & ~3;
    } else {
        int offset = (cursor_y * SCREEN_WIDTH + cursor_x) * 2;
        video[offset] = c;
        video[offset + 1] = WHITE_ON_BLACK;
        cursor_x++;
    }

    /* 换行 */
    if (cursor_x >= SCREEN_WIDTH) {
        cursor_x = 0;
        cursor_y++;
    }

    scroll();
}

/* 打印字符串 */
void print_string(const char *str) {
    while (*str) {
        print_char(*str);
        str++;
    }
}

/* 内核入口 */
void kernel_main(void) {
    clear_screen();
    print_string("Welcome to My OS!\n");
    print_string("Initializing IDT...\n");

    idt_init();
    print_string("IDT initialized.\n");

    print_string("Initializing keyboard...\n");
    keyboard_init();
    print_string("Keyboard initialized.\n\n");

    print_string("Type something: ");

    /* 开启中断 */
    __asm__ __volatile__("sti");

    /* 主循环 */
    while (1) {
        __asm__ __volatile__("hlt");  /* 等待中断，省电 */
    }
}