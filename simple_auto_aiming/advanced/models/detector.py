from models import config as con
import random
def detect():
    num = random.randint(0,3)
    targets = []              #空列表，准备一个篮子
    for _ in range(num):
        x = random.randint(-con.COORD_RANGE,con.COORD_RANGE)
        y = random.randint(-con.COORD_RANGE,con.COORD_RANGE)
        targets.append((x,y)) #逐步在列表中添加元素

    return targets

if __name__ == "__main__":    #绝对导入使得运行路径错误，需改回平级： 删去from models
     print(f"测试 detector 模块： {detect()}")
   
