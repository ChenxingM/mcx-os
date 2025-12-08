# CLAUDE.md - Project Guide for AI Assistants

## Project Overview

**mcxOS** is an educational operating system built from scratch to learn computer architecture fundamentals. It includes a bootloader, protected mode switching, and a basic C kernel with VGA text output.

## Directory Structure

```
mcx-os/
├── src/
│   ├── boot/           # Bootloader and boot code (x86 assembly)
│   │   ├── boot.asm    # Main bootloader (512 bytes, org 0x7c00)
│   │   ├── disk.asm    # Disk reading functionality
│   │   ├── gdt.asm     # Global Descriptor Table
│   │   ├── kernel_entry.asm  # 32-bit kernel entry point
│   │   └── switch_pm.asm     # Protected mode switching
│   └── kernel/
│       └── kernel.c    # C kernel (VGA output)
├── build/              # Build output (generated)
├── scripts/
│   └── setup.sh        # Environment setup script
└── Makefile            # Build configuration
```

## Build Commands

```bash
make          # Build the OS image
make run      # Build and run in QEMU
make debug    # Build with debug symbols and run with GDB
make clean    # Clean build artifacts
```

## Languages & Tools

- **x86 Assembly** (NASM, Intel syntax) - bootloader and mode switching
- **C** (freestanding, no stdlib) - kernel implementation
- **Cross-compiler**: i686-elf-gcc (macOS) or gcc -m32 (Linux)
- **Emulator**: QEMU (qemu-system-i386)

## Key Technical Details

### Memory Layout
- Boot sector: `0x7c00` (BIOS standard)
- Kernel load address: `0x1000`
- Stack top: `0x9000`
- VGA memory: `0xB8000`

### Boot Process
1. BIOS loads 512-byte boot sector at 0x7c00
2. Bootloader loads kernel to 0x1000
3. Switch from 16-bit real mode to 32-bit protected mode
4. Jump to kernel_main()

### Compile Flags
```
-m32 -ffreestanding -fno-pie -nostdlib -fno-builtin -fno-stack-protector
```

## Coding Conventions

### Assembly
- Chinese comments for documentation
- Uppercase labels: `KERNEL_OFFSET`, `BOOT_DRIVE`
- Lowercase functions: `print_string`, `disk_load`
- Section headers with ASCII art borders

### C
- Constants as macros: `#define VIDEO_MEMORY 0xB8000`
- Direct hardware memory access
- No abstraction layers (educational simplicity)

## Development Notes

- Primary platform: macOS (cross-compiling to i386)
- Also supports: Linux, Windows (WSL)
- Documentation language: Chinese
