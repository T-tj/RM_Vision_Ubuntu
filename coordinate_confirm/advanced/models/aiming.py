def calculate_offset(target,center):
    offset_x = target[0]-center[0]
    offset_y = target[1]-center[1]
    return(offset_x,offset_y)

def decide_direction(offset):
    offset_x = offset[0]
    offset_y = offset[1]

    if offset_x > 10:
        instruction_x = "往右看"
    elif offset_x < -10:
        instruction_x = "往左看"
    else:
        instruction_x = "横向保持"

    if offset_y > 10: 
        instruction_y = "往下看"
    elif offset_y < -10:
        instruction_y = "往上看"
    else:
        instruction_y = "纵向保持"

    return(instruction_x,instruction_y)

def is_near_center(offset):
    offset_x = offset[0]
    offset_y = offset[1]

    # if -10 <= offset_x <=10 and -10 <= offset_y <= 10:
    #     return True
    # else:
    #     return False
    if abs(offset_x) <= 10 and abs(offset_y) <= 10:
        return True
    else:
        return False

if __name__ == "__main__":
    print(calculate_offset((210, 60), (150, 100)))
    print(decide_direction((60, -40)))
    print(is_near_center((10, -10)))
    print(is_near_center((0, 40)))