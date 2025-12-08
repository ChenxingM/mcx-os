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

# C 源文件
C_SOURCES = $(wildcard $(SRC)/kernel/*.c)
C_OBJECTS = $(patsubst $(SRC)/kernel/%.c, $(BUILD)/%.o, $(C_SOURCES))

# 内核汇编
KERNEL_ASM = $(SRC)/kernel/isr.asm
KERNEL_ASM_OBJ = $(BUILD)/isr_asm.o

.PHONY: all clean run debug

all: $(BUILD)/os-image.bin

$(BUILD):
	mkdir -p $(BUILD)

# 引导扇区
$(BUILD)/boot.bin: $(SRC)/boot/boot.asm $(SRC)/boot/disk.asm $(SRC)/boot/gdt.asm $(SRC)/boot/switch_pm.asm | $(BUILD)
	$(ASM) -f bin -I $(SRC)/boot/ $< -o $@

# 内核入口
$(BUILD)/kernel_entry.o: $(SRC)/boot/kernel_entry.asm | $(BUILD)
	$(ASM) -f elf $< -o $@

# ISR 汇编
$(BUILD)/isr_asm.o: $(SRC)/kernel/isr.asm | $(BUILD)
	$(ASM) -f elf $< -o $@

# C 文件编译
$(BUILD)/%.o: $(SRC)/kernel/%.c | $(BUILD)
	$(CC) $(CFLAGS) $< -o $@

# 链接内核
$(BUILD)/kernel.bin: $(BUILD)/kernel_entry.o $(KERNEL_ASM_OBJ) $(C_OBJECTS)
	$(LD) $(LDFLAGS_ARCH) -o $@ -Ttext 0x1000 $^ --oformat binary

# 生成镜像
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