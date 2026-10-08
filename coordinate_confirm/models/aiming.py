def calculate_offset_x(target,center):
    result =  target[0] - center[0]
    return result

def decide_horizontal(offset_x):
    if offset_x > 10:
        result =  "向右看"
    elif offset_x < -10:
        result =  "向左看"
    else:
        result =  "横向保持"
    return result

if __name__ =="__main__":
    test_offset = calculate_offset_x((210,60),(150,100))
    print("测试偏差: ",test_offset)
    print("测试方向：",decide_horizontal(test_offset))