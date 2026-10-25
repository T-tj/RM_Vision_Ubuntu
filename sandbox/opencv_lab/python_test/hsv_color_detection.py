import cv2
import numpy as np

img = cv2.imread("../data/Black-winged_Kite.jpg")
if img is None:
    print("读取失败，请检查路径")
    exit()
else:
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,100,70])
    upper_blue = np.array([124,255,255])

    mask = cv2.inRange(hsv,lower_blue,upper_blue)

    result = cv2.bitwise_and(img,img,mask = mask)
    cv2.imwrite("../output_py/mask_kite_put.jpg",mask)
    cv2.imwrite("../output_py/blue_kite_put.jpg",result)
    print("✅ 成功保存 mask_kite_put.jpg 和 blue_kite_put.jpg")