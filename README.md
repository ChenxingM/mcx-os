# My OS

从零开始编写的操作系统，用于学习计算机底层原理。

## 环境要求

- macOS / Linux / Windows (WSL)
- 交叉编译器 (i686-elf-gcc)
- NASM 汇编器
- QEMU 模拟器

## 快速开始

```bash
# 安装依赖
chmod +x scripts/setup.sh
./scripts/setup.sh

# 编译
make

# 运行
make run

# 清理
make clean
```

## 项目结构

```
my-os/
├── Makefile          # 构建脚本
├── src/
│   ├── boot/
│   │   ├── boot.asm         # 引导扇区 (第一课)
│   │   └── kernel_entry.asm # 内核入口 (第二课)
│   └── kernel/
│       └── kernel.c         # 内核主程序 (第三课)
├── scripts/
│   └── setup.sh      # 环境安装脚本
└── build/            # 编译输出
```

## 学习路线

1. **Lesson 1**: 引导扇区 - 在屏幕上打印字符
2. **Lesson 2**: 进入保护模式 - 从 16 位到 32 位
3. **Lesson 3**: C 语言内核 - 实现 VGA 文本输出
4. **Lesson 4**: 中断处理 - 响应键盘输入
5. **Lesson 5**: 内存管理 - 实现简单的分配器

## 参考资料

- [OSDev Wiki](https://wiki.osdev.org)
- [os-tutorial](https://github.com/cfenollosa/os-tutorial)
- [Writing an OS in Rust](https://os.phil-opp.com)
