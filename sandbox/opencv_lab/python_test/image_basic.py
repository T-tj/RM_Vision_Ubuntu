import cv2

#注意路径：从根目录执行，指向lena.jpg
img = cv2.imread('../data/lena.jpg')
if img is None:
    print("读取失败,请确认图片路径正确")
    exit()
print("彩色图形状：",img.shape)


# 色彩通道分离

# 1.将原图分离为 B,G,R 三个单通道
b_channel,g_channel,r_channel = cv2.split(img)
# 2.统计各个通道像素值总和（验证颜色强度）
b_sum= b_channel.sum()
print(f"B通道像素值总和: {b_sum}")
# 3.保存分离出的通道图
cv2.imwrite("../output_py/channel_B.jpg",b_channel)
cv2.imwrite("../output_py/channel_G.jpg",g_channel)
cv2.imwrite("../output_py/channel_R.jpg",r_channel)
print("✅ 已保存 B,G,R 三个通道的分离图片")


# 转为灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
print("灰度图形状：",gray.shape)

# 二值化转换灰度图
# retval 是实际使用的阙值， thresh 是处理后的黑白图像
retval,thresh = cv2.threshold(b_channel,97,255,cv2.THRESH_BINARY)
cv2.imwrite("../output_py/thresh_binary.jpg",thresh)
print("✅ 已保存二值化图片，使用的阙值为：{rtval}")

# 图片缩放
resized = cv2.resize(gray,(337,227))
print("缩放后形状：",resized.shape)

# cv2.imshow("image_gray",gray)  # 弹窗
# cv2.waitKey(0)  # 等待用户按下按键再消除弹窗
# cv2.destoryALLWindows()  # 消除所有弹窗

#保存缩放结果至output_py
cv2.imwrite("../output_py/gray_output.jpg",gray)
cv2.imwrite("../output_py/resized_output.jpg",resized)
print("✅ 已保存 gray_output.jpg 和 resized_output.jpg")