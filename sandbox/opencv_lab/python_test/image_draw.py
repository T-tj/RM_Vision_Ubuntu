import cv2
img = cv2.imread('../data/Black-winged_Kite.jpg')
if img is None:
    print("读取失败,请确认图片路径正确")
    exit()
    print("彩色图形状：",img.shape)

# 绘制线条
img_line = cv2.line(img,(50,50),(570,570),(0,255,0),3)
# 绘制圆
img_circle = cv2.circle(img_line,(370,170),50,(0,0,255),77)
# 绘制矩形
img_rectangle = cv2.rectangle(img_circle,(70,70),(270,270),(70,170,177),7)
# 绘制文字
out = cv2.putText(img_rectangle,"Hello",(70,270),cv2.FONT_HERSHEY_SIMPLEX,7,(255,255,255),1)

cv2.imwrite('../output_py/Black-winged_out.jpg',out)
print("已保存 Black-winged_out.jpg")