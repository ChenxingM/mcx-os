# Project: mcxOS

## 项目概述
从零编写操作系统，学习计算机底层原理。

## 技术栈
- 语言：C + x86 汇编 (NASM)
- 工具链：i686-elf-gcc (交叉编译器)
- 模拟器：QEMU
- 构建：Make

## 开发环境
- 主要在 macOS (M4 MacBook Air) 开发
- 跨平台支持：macOS / Linux / WSL

## 学习进度
- [ ] Lesson 1: 引导扇区 - 打印字符
- [ ] Lesson 2: 保护模式 - 16位到32位
- [ ] Lesson 3: C 内核 - VGA 文本输出
- [ ] Lesson 4: 中断处理
- [ ] Lesson 5: 内存管理

## 当前任务
正在学习 boot.asm - 实现引导扇区，在屏幕打印字符。

## 编码偏好
- 中文注释
- 详细解释底层原理
- 循序渐进，先理解再动手

## 构建命令
```bash
make        # 编译
make run    # 运行
make clean  # 清理
```