# ===========================================
# My OS - Makefile
# ===========================================

UNAME := $(shell uname -s)

ifeq ($(UNAME), Darwin)
    CC = i686-elf-gcc
    LD = i686-elf-ld
else ifeq ($(UNAME), Linux)
    CC = gcc
    LD = ld
    CFLAGS_ARCH = -m32
    LDFLAGS_ARCH = -m elf_i386
endif

ASM = nasm
QEMU = qemu-system-i386

CFLAGS = $(CFLAGS_ARCH) -ffreestanding -fno-pie -nostdlib \
         -fno-builtin -fno-stack-protector -Wall -Wextra -c -g

BUILD = build
SRC = src

.PHONY: all clean run debug

all: $(BUILD)/os-image.bin

# 创建 build 目录
$(BUILD):
	mkdir -p $(BUILD)

# 编译引导扇区（包含其他 asm 文件）
$(BUILD)/boot.bin: $(SRC)/boot/boot.asm $(SRC)/boot/disk.asm $(SRC)/boot/gdt.asm $(SRC)/boot/switch_pm.asm | $(BUILD)
	$(ASM) -f bin -I $(SRC)/boot/ $< -o $@

# 编译内核入口
$(BUILD)/kernel_entry.o: $(SRC)/boot/kernel_entry.asm | $(BUILD)
	$(ASM) -f elf $< -o $@

# 编译 C 内核
$(BUILD)/kernel.o: $(SRC)/kernel/kernel.c | $(BUILD)
	$(CC) $(CFLAGS) $< -o $@

# 链接内核
$(BUILD)/kernel.bin: $(BUILD)/kernel_entry.o $(BUILD)/kernel.o
	$(LD) $(LDFLAGS_ARCH) -o $@ -Ttext 0x1000 $^ --oformat binary

# 合并引导扇区和内核
$(BUILD)/os-image.bin: $(BUILD)/boot.bin $(BUILD)/kernel.bin
	cat $^ > $@
	@echo ""
	@echo "✓ Build complete: $@"
	@echo ""

run: $(BUILD)/os-image.bin
	$(QEMU) -fda $(BUILD)/os-image.bin

debug: $(BUILD)/os-image.bin
	$(QEMU) -fda $(BUILD)/os-image.bin -s -S &
	sleep 1
	gdb -ex "target remote localhost:1234" -ex "set architecture i386"
clean:
	rm -rf $(BUILD)