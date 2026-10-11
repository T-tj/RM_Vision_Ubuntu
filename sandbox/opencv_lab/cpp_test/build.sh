#!/bin/bash
# 工业级一键构建脚本

# 如果 build 目录不存在，则创建并进入
if [ ! -d "build" ]; then
    mkdir build
fi
cd build

# 运行 cmake 配置并编译（-j 代表多线程编译，提速）
cmake ..
make -j4

echo "✅ 编译完成！"
