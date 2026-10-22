#1.
name = "周小明"
age = 18 
hobby = "爱打游戏"
print("我的名字是小明,今年18岁,爱打游戏。")
num = "123"
num1 = int(num)+7
print(num1)


#2.
num = int(input("请输入一个整数："))
if num > 0:
    print("正数")
elif num < 0:
    print("负数")
else:
    print("零")

score = float(input("请输入考试分数: "))
if score >= 90:
    print("优秀")
elif score >= 70:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")


#3
for i in range(1,11):
    print(i)

sum = 0
j = 1
while j <= 100: 
    sum += j
    j += 1
print(sum)


#4
robot = {
    "name" : "步兵",
    "number" : 3,
    "ready" : True
}
print(f"{robot['number']}号步兵，准备状态：{robot['ready']}")
robot["ready"] = False
print(f"{robot['number']}号步兵，准备状态：{robot['ready']}")


#5
def add(a, b):
    result = a + b
    return result
print(add(7,6))

def greet(name):
    print(f"你好，{name}")
greet("小明")


#6