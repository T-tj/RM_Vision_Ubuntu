# Simple Auto-Aiming Framework (简化瞄准框架)

## 📖 项目简介
本项目是一个用于模拟真实场景（如 RoboMaster 视觉算法）的**简化瞄准框架**。
真实比赛的视觉算法涉及相机标定、光照补偿、装甲板识别等复杂工程。本项目的目标是**剥离外围环境，将核心瞄准逻辑简化为二维坐标的“检测 -> 计算 -> 判定 -> 输出”流水线**。

项目分为 **基础版（basic）** 和 **升级版（advanced）** 两个独立模块，用以展示从“处理单目标”到“多目标批量处理与实时循环”的架构演进。

## 📁 项目结构
```text
simple_auto_aiming/
├── basic/                          # 基础版（单目标处理）
│   ├── main.py                     # 入口调度：串联检测、计算、打印
│   └── models/                     # 核心逻辑包
│       ├── __init__.py             # 包标识文件
│       ├── config.py               # 参数配置（THRESHOLD = 3）
│       ├── detector.py             # 模拟检测：随机生成单个坐标
│       ├── geometry.py             # 几何计算：单目标距离 + 击打判定
│       └── utils.py                # 打印工具：格式化输出
│
└── advanced/                       # 升级版（多目标 + 实时循环）
    ├── main.py                     # 入口调度：含 1Hz 主事件循环
    └── models/
        ├── __init__.py             # 包标识文件
        ├── config.py               # 参数配置（THRESHOLD, COORD_RANGE）
        ├── detector.py             # 模拟检测：随机生成 0~3 个目标
        ├── geometry.py             # 几何计算：批量距离 + 选最近 + 判定
        └── utils.py                # 打印工具：格式化输出
```

💻 运行环境

· 操作系统：Ubuntu 22.04 / Windows / macOS
· Python 版本：3.10.12 及以上
· 依赖库：本项目仅使用 Python 标准库（math, random, time），无需安装任何第三方包，开箱即用。

🚀 快速开始

在终端进入对应的版本目录，使用 Python 3 运行：

1. 基础版（处理单个目标）

```bash
cd basic
python3 main.py
```

2. 升级版（多目标 + 实时刷新，按 Ctrl+C 退出）

```bash
cd advanced
python3 main.py
```

📊 示例输出

基础版输出：

```text
center: (4, 4) - distance: 5 - attackable: False
```

升级版输出（多目标与空目标异常处理）：

```text
center: [(2, 1), (5, -3)] - distances: [2, 5] - closest: 2 - attackable: True
center: [(7, -8)] - distances: [10] - closest: 10 - attackable: False
center: [] - distances: [] - closest: None - attackable: False
```

🧠 核心设计原则

1. 参数与逻辑分离：所有可变参数（如击打阈值 THRESHOLD、坐标随机范围 COORD_RANGE）统一存放在 config.py。修改参数无需触碰底层逻辑代码。
2. 单一职责原则：detector 只负责模拟产生数据，geometry 只负责数学运算与判定，utils 只负责格式化输出，main 只负责调度串联。
3. 绝对导入与命名空间：使用 from models import xxx 绝对导入，杜绝命名冲突，保证大型项目可维护性。
4. 防御性编程：在 geometry.py 中，针对空列表和 None 值做了严格拦截（如 if not distances: return None 以及 if closest is None: return False），确保系统在异常状况下不会崩溃。
5. 实时系统架构：advanced/main.py 采用 while True + time.sleep(1) 构建主事件循环，并利用 ANSI 转义序列（\033[H\033[J）实现终端雷达式无闪烁清屏，模拟 1Hz 的实时检测频率。

📈 架构演进

· Basic（基础版）：处理单个目标，侧重于“检测 -> 计算 -> 判定”单线程流水线的跑通。
· Advanced（升级版）：处理 0~3 个随机目标，增设“找出最近目标”逻辑，并在 main.py 中引入 while True 主事件循环与 ANSI 清屏，模拟 1Hz 实时识别与打击的机器人应用场景。

📝 踩坑记录与成长

· 路径地狱：最初直接运行子模块（如 python3 geometry.py）导致 ModuleNotFoundError。解决方案是遵守工程规范，只从顶层入口 main.py 运行，子模块仅暴露函数供调用。
· 防御性编程缺失：空列表或空目标传给 min() 或比较运算符时会导致程序崩溃。通过在 geometry.py 中增加 is None 和 not distances 检查，增强了程序健壮性。
· 开发环境：在 Ubuntu 22.04 虚拟机（VS Code 远程 SSH）中完成开发，全程贯彻工软规范。

👨‍💻 作者与许可

· District46战队算法组
· 许可证：本项目仅供学习与培训使用，遵循 MIT 许可协议。
```