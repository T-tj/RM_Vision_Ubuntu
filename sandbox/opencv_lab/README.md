```markdown
# OpenCV 环境搭建与基础读取练习 (C++ / Python)

## 📖 项目简介
本项目用于在 Ubuntu 22.04 环境下，完成 OpenCV 的安装、C++ 与 Python 双语言环境配置，并实现基础的图像读取与验证。

## 📁 项目结构
```text
opencv_lab/
├── cpp_test/              # C++ 测试模块
│   ├── .vscode/           # 编辑器调试与任务配置
│   ├── build/             # CMake 构建输出目录（已在 .gitignore 中忽略）
│   ├── CMakeLists.txt     # CMake 工程配置
│   ├── read_image.cpp     # C++ 图像读取测试代码
│   ├── build.sh           # 一键构建脚本
│   └── run.sh             # 一键编译+运行脚本
├── data/                  # 测试图片资源目录
└── python_test/           # Python 测试模块
    └── read_image.py      # Python 图像读取测试代码
```

🚀 运行指南

1. C++ 版本（需通过 CMake 编译）

```bash
cd cpp_test
./build.sh      # 仅编译
./run.sh        # 编译并运行（需要先赋予执行权限：chmod 755 run.sh build.sh）
```

2. Python 版本（解释型，直接运行）

```bash
cd python_test
python3 read_image.py
```

🧠 核心设计思路与工程规范

1. 多根工作区（Multi-root Workspace）：使用 rm_vision.code-workspace 管理项目，使 C++ 项目（cpp_test）拥有独立的 .vscode 配置，与 Python 练习完全隔离，互不干扰。
2. 构建脚本化：拒绝手动敲 cmake .. && make，通过 build.sh 和 run.sh 实现自动化，并强制使用 make -j4 多线程编译提升效率。
3. 动态绝对路径（Python）：使用 os.path.abspath(__file__) 动态获取当前脚本位置，避免因终端工作目录不同导致图片读取失败，实现“在哪都能跑”。
4. 相对路径（C++）：通过固定 build 工作目录，使用 ../../data/ 定位图片资源，这也是 C++ 工程中通过 cwd 解决路径问题的标准方式。

📝 踩坑记录与成长（工业实战）

· 权限地狱：在 Linux 中直接执行 ./run.sh 报错 Permission denied。
  · 解决：使用 chmod 755 run.sh 补全“读写执行”权限。不要只加 +x，否则系统无法读取脚本头部导致依然报错。
· SSH 环境无图形界面：cv2.imshow() 报错 qt.qpa.xcb: could not connect to display。
  · 解决：在 SSH 远程终端中，因无图形界面环境，需注释掉 imshow 相关代码，改用 cv2.imwrite 保存处理结果，这也是真实工业“无头服务器”的标准做法。
· C++ 路径与工作目录：在 build 目录下运行时，必须确保 launch.json 中的 cwd 为 build，否则 ../../data/ 的相对路径会失效。

```

---