#硬编码参数
center = (150, 100)
target = (210,60)  #此时target【0】是目标的x坐标,target[1]是目标的y坐标


#输入与输出
x_text= input("请输入x坐标: ")  #input()函数获取用户输入，返回值为字符串类型
y_text= input("请输入y坐标: ")  
x = int(x_text)  #将字符串转换为整数
y = int(y_text) 
target = (x, y)  #将用户输入的坐标赋值给target  在这里元组并未被修改，target只是更换了指向对象        #####
print("当前目标坐标为:", target)  #打印输出目标坐标

#f-string格式化输出
print (f"目标的横坐标是 {x},纵坐标是 {y}")  #f-string格式化输出，f-string中可以直接使用变量


offset_x = target[0] - center[0]  #计算目标相对于中心点的偏移量
offset_y = target[1] - center[1]
print(f"目标相对于中心点的偏移量为: ({offset_x}, {offset_y})")  #打印输出偏移量


#比较运算符会给出一个boolean值，True或False,让偏差变为判断
print(offset_x > 0)  #判断目标是否在中心点的右侧
print(offset_y > 0)  #判断目标是否在中心点的下方

#if
# if offset_x > 0:
#     print("向右看")
# elif offset_x < 0:
#     print("向左看")
# else:
#     print("横向不用调整")


#组合多个条件
near_x= -10 <= offset_x <= 10  #判断目标是否在中心点的左右10个像素范围内
near_y= -10 <= offset_y <= 10  #判断目标是否在中心点的上下10个像素范围内
if near_x and near_y:
    print("目标在中心点附近,不需要调整")
else:
    print("目标不在中心点附近,需要调整")



#循环：处理多个目标
targets = [(210, 60), (90, 140), (150, 100)]  # 假设有多个目标坐标
for target in targets:                        #for循环遍历每个目标坐标给target
    offset_x = target[0] - center[0]
    offset_y = target[1] - center[1]
    #print（"当前目标",target)
    print(f"当前目标: {target}, 偏移量: ({offset_x}, {offset_y})")
    if offset_x > 0:
        print("向右看")
    elif offset_x < 0:
        print("向左看")
    else:
        print("横向不用调整")

    if offset_y > 0:
        print("向下看")
    elif offset_y < 0:
        print("向上看")
    else:
        print("纵向不用调整")


#range()  无需列表也能重复执行 ,配合for循环使用，控制次数                                    
for i in range(5):         #range(5)生成一个从0到4的整数序列，for循环会依次将这些整数赋值给i
    print(i)
    print("Hello World")   #打印5次Hello World
#range(start,stop,step)还可以指定起始值和步长  
for i in range(1, 10, 2):  #生成一个从1到9的奇数序列
    print(i)
for i in range(2,7):
    print(i)
#range()不会输出stop值


#while循环  当条件为True时，循环继续执行，当条件为False时，循环结束
count = 0
while count < 7:            #当count小于7时，循环继续执行
    print(count)
    count += 1  #count = count + 1


#break与continue            #break用于跳出(终止）循环，continue用于跳过本次循环，继续下一次循环
while True:
    text = input("请输入目标的x坐标,输入q退出: ")
    if text == "q":
        break
    x = int(text)
    if x < 0 or x > 300:    #假设屏幕宽度为300像素，若输入的x坐标不在屏幕范围内，则跳过本次循环
        print("输入的x坐标不在屏幕范围内,请重新输入")
        continue
    print(f"收到目标的横坐标为: {x}")

print("本次输入结束")



#用def定义函数
def say_hello():
    print("Hello World!")

say_hello()  #调用函数

def greet(name):
    print(f"Hello, {name}!")

greet("明")                  #调用函数并传入参数
greet("小明")                #参数修改

#用return将处理结果交回调用处
def add(a, b):
    result = a + b
    return result

answer = add(5, 3)
print(answer)                # 输出 8

