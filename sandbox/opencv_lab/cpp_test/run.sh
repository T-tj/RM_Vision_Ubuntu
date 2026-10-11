#!/bin/bash
set -e  # 遇到错误立即停止执行

# 1. 调用编译脚本
echo "🔨 开始编译..."
./build.sh

# 2. 进入 build 目录并运行，支持把外部参数传进去
echo "🚀 正在运行程序..."
cd build
./main "$@"