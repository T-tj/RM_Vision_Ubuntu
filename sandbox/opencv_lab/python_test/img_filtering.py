import cv2

#1.读取原图（注意路径：从根目录执行，指向sandbox/data/workers.jpg）
img = cv2.imread('../data/lena.jpg')
if img is None:
    print("读取失败,请取人图片路径正确")
    exit()

#2.转灰度图，滤波通常在灰度图上做
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#3.高斯模糊（卷积核(5,5),必须是奇数）
gaussian = cv2.GaussianBlur(gray,(5,5),0)
cv2.imwrite("../output_py/gaussian_output.jpg",gaussian)

#4.中值滤波（对椒盐噪声有效）
median = cv2.medianBlur(gray,9)
cv2.imwrite("../output_py/median_output.jpg",median)

#5.边缘检测（先模糊再Canny,减少噪声假边缘）
edges = cv2.Canny(gaussian,50,150)
cv2.imwrite("../output_py/edges_output.jpg",edges)

print("已保存 gaussian_output.jpg,median_output.jpg,edges_output.jpg")
