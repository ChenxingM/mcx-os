#!/bin/bash

set -e

echo "=== My OS Development Environment Setup ==="
echo ""

case "$(uname -s)" in
    Darwin)
        echo "[*] macOS detected"
        
        if ! command -v brew &> /dev/null; then
            echo "[*] Installing Homebrew..."
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        fi
        
        echo "[*] Installing dependencies..."
        brew install i686-elf-gcc i686-elf-gdb nasm qemu make
        
        echo ""
        echo "✓ Setup complete!"
        ;;
        
    Linux)
        echo "[*] Linux detected"
        
        if command -v apt &> /dev/null; then
            echo "[*] Using apt..."
            sudo apt update
            sudo apt install -y build-essential nasm qemu-system-x86 gdb
        elif command -v pacman &> /dev/null; then
            echo "[*] Using pacman..."
            sudo pacman -S --noconfirm base-devel nasm qemu gdb
        else
            echo "[!] Unknown package manager"
            echo "    Please install: gcc, nasm, qemu-system-x86, gdb"
            exit 1
        fi
        
        echo ""
        echo "✓ Setup complete!"
        ;;
        
    *)
        echo "[!] Unsupported platform: $(uname -s)"
        exit 1
        ;;
esac

echo ""
echo "Next steps:"
echo "  make        - Build the OS"
echo "  make run    - Run in QEMU"
echo "  make clean  - Clean build files"
