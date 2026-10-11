#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    // 1. 读取图片
    std::string image_path = "../../data/lena.jpg";
    cv::Mat img = cv::imread(image_path);

    // 2. 校验是否读取成功
    if (img.empty()) {
        std::cout << "❌ 错误：无法读取图片，请检查路径: " << image_path << std::endl;
        return -1;
    }

    std::cout << "✅ 成功读取图片!" << std::endl;
    std::cout << "图片尺寸 (宽 x 高): " << img.cols << "x" << img.rows << std::endl;

    // 3. 显示图片
    cv::imshow("C++ Read Image", img);
    cv::waitKey(0);
    cv::destroyAllWindows();

    // 4. 备用验证：保存图片
    cv::imwrite("../data/lena_cpp_out.jpg", img);

    return 0;
}