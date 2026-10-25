import cv2
import numpy as np

# ==========================================
# 任务 1：对 Black-winged_Kite 做边缘与轮廓检测
# ==========================================
print("--- 开始处理 Black-winged_Kite.jpg ---")
img_kite = cv2.imread('../data/Black-winged_Kite.jpg')
if img_kite is None:
    print("❌ 无法读取 Black-winged_Kite.jpg")
else:
    # 1. 转灰度与高斯模糊（降噪，边缘检测前必须做）
    gray_kite = cv2.cvtColor(img_kite, cv2.COLOR_BGR2GRAY)
    blurred_kite = cv2.GaussianBlur(gray_kite, (5, 5), 0)

    # 2. Canny 边缘检测
    # 50 和 150 是高低阈值，可根据实际图片亮度微调
    edges_kite = cv2.Canny(blurred_kite, 50, 150)
    cv2.imwrite("../output_py/kite_edges.jpg", edges_kite)

    # 3. 轮廓检测
    # 必须传入二值图（这里用 edges_kite），RETR_EXTERNAL 只找最外层轮廓
    contours_kite, _ = cv2.findContours(edges_kite.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
    # 在原图上画出轮廓（红线条，粗细2）
    img_kite_contours = img_kite.copy()
    cv2.drawContours(img_kite_contours, contours_kite, -1, (0,0,255), 5)
    cv2.imwrite("../output_py/kite_contours.jpg", img_kite_contours)
    print(f"✅ 黑鸢图片处理完成，检测到 {len(contours_kite)} 个轮廓")


# ==========================================
# 任务 2：对 2027 做轮廓与线段检测
# ==========================================
print("\n--- 开始处理 2027.jpg ---")
# 注意：如果你的文件是 webp，请把下面的 jpg 改成 webp
img_2027 = cv2.imread('../data/2027.jpg') 
if img_2027 is None:
    print("❌ 无法读取 2027.jpg，请检查文件名")
else:
    gray_2027 = cv2.cvtColor(img_2027, cv2.COLOR_BGR2GRAY)
    blurred_2027 = cv2.GaussianBlur(gray_2027, (5, 5), 0)
    edges_2027 = cv2.Canny(blurred_2027, 50, 150)

    # 1. 轮廓检测
    contours_2027, _ = cv2.findContours(edges_2027.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    img_2027_contours = img_2027.copy()
    cv2.drawContours(img_2027_contours, contours_2027, -1, (0, 0, 255), 2) # 红色轮廓
    cv2.imwrite("../output_py/2027_contours.jpg", img_2027_contours)
    print(f"✅ 2027图片轮廓检测完成，检测到 {len(contours_2027)} 个轮廓")

    # 2. 线段检测（概率霍夫变换 HoughLinesP）
    # 参数：边缘图, 距离精度(像素), 角度精度(弧度), 阈值(超过多少个点才认为是线), 最短线段长度, 允许断开的间隙
    lines = cv2.HoughLinesP(edges_2027, 1, np.pi / 180, threshold=30, minLineLength=20, maxLineGap=5)
    
    img_2027_lines = img_2027.copy()
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.ravel()
            # 画出线段（蓝色，粗细2）
            cv2.line(img_2027_lines, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.imwrite("../output_py/2027_lines.jpg", img_2027_lines)
        print(f"✅ 2027图片线段检测完成，检测到 {len(lines)} 条线段")
    else:
        print("❌ 未检测到任何线段，请尝试调低 threshold 或 minLineLength")

print("\n🎉 所有处理完毕！请去 output_py 文件夹查看图片。")
    