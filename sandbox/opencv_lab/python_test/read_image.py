import cv2
import os

# 1. 获取当前脚本所在目录的绝对路径（锚定在 python_test/ 下）
base_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 基于脚本自身位置，去上一级找 data 目录（../data/lena.jpg）
image_path = os.path.join(base_dir, '..', 'data', 'lena.jpg')

# 3. 读取图片
img = cv2.imread(image_path)

# 2. 校验是否读取成功
if img is None:
    print(f"❌ 错误：无法读取图片，请检查路径: {image_path}")
else:
    print(f"✅ 成功读取图片!")
    print(f"图片尺寸 (高 x 宽 x 通道): {img.shape}")
    
    # 3. 显示图片（适用于有图形界面的环境）
    # cv2.imshow("Python Read Image", img)
    # cv2.waitKey(0)  # 等待按键
    # cv2.destroyAllWindows()
    
    # 4. 备用验证：保存一张图片以防无法弹窗显示
    cv2.imwrite(os.path.join(base_dir, '..', 'data', 'lena_python_out.jpg'), img)