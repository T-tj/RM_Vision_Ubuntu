import random
def detect():
    x = random.randint(-10,10)
    y = random.randint(-10,10)
    return(x,y)

if __name__ == "__main__":
    print(f"测试 detector 模块： {detect()}")
    print(f"测试 detector 模块： {detect()}")