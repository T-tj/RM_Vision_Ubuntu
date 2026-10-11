# 声明 CMake 最低版本要求
cmake_minimum_required(VERSION 3.10)

# 项目名称
project(OpenCV_Test)

# 设置 C++ 标准
set(CMAKE_CXX_STANDARD 14)

# 查找 OpenCV 库（必须）
find_package(OpenCV REQUIRED)

# 包含头文件目录（可选但推荐）
include_directories(${OpenCV_INCLUDE_DIRS})

# 指定生成的可执行文件（名称 main，源文件 main.cpp）
add_executable(main read_image.cpp)

# 链接 OpenCV 库
target_link_libraries(main ${OpenCV_LIBS})