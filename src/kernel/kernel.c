/* ===========================================
* kernel.c - 内核主程序
 * =========================================== */

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

/* 打印单个字符 */
void print_char(char c) {
    char *video = (char *)VIDEO_MEMORY;

    if (c == '\n') {
        cursor_x = 0;
        cursor_y++;
    } else {
        int offset = (cursor_y * SCREEN_WIDTH + cursor_x) * 2;
        video[offset] = c;
        video[offset + 1] = WHITE_ON_BLACK;
        cursor_x++;

        if (cursor_x >= SCREEN_WIDTH) {
            cursor_x = 0;
            cursor_y++;
        }
    }
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
    print_string("Hello from C Kernel!\n");
    print_string("Welcome to your own OS!\n");

    while (1) {
        /* 主循环 */
    }
}