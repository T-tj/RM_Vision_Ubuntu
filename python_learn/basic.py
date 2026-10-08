print("Hello world!")

#Variable（变量）
name = "明"
age = 18 
print (name,age)
age = age+1
print(age)
age = 26  #整数 （int）
sleep_hours = 8.46  #浮点数 （float）

#python中无需声明变量类型，变量类型会根据赋值自动推断
num:int = 10  #若想表明类型可使用 类型注解
num = 10
print(num)

sleep = True       #值为1
play_game = False  #值为0
if sleep:          #True 可用整数代替，对于整数，0为False，非0为True
    print("睡觉")
else:
    print("玩游戏")



#List（列表）
information = ["明", 18, 1.75]
print(information)
print(information[0])  #索引从0开始
print(information[1])
print(information[2])
print(information[-1])  #索引从-1开始，-1表示最后一个元素   
information[-1] = 1.83  #修改列表中的元素
print(information[-1])
information = [1, 2, 3, 4, 5]
print(information)
information = 2
print(information)  #列表被覆盖，变为整数
information = [1, 2, 3, 4]
information.append(5)  #在列表末尾添加元素，无专门指定头部的方法
print(information)
information.insert(0, 0)  #在指定位置插入元素 insert(索引位置，要插入的元素)
print(information)
information.remove(3)  #删除指定元素（从左到右删除第一个匹配的元素）
print(information)



#Tuple（元组）   #元组与列表类似，区别在于元组的元素不能替换增改，元组使用小括号()表示
number = (2,3)  #主要用于表达一组位置固定，各位置有确定含义的数据。eg.坐标，RGB颜色值等
print(number)
print(number[0])
print(number[1])



#Dictionary（字典）  #字典是无序的键值对（键（key）：值（value）），使用大括号{}表示
student = {
    "name": "明",
    "age": 18,
    "height": 1.75,
    "sleep_hours": 8.46
    }  #字典就像一个登记表，给每一项数据写上名字，而不用记第几个位置上放了什么
print(student)
print(student["name"])        #通过键访问值   
print(student["sleep_hours"])
student["age"] = 19           #修改字典中的值
student["play_game"] = True   #添加新的键值对
print(student["age"])
print(student["play_game"])
#print(student["weight"])     #访问不存在的键会报错 KeyError: 'weight'
print("weight" in student)    #可先判断字典中是否存在某个键，返回布尔值


