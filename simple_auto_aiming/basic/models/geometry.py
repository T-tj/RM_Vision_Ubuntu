from models import config
import math
def calculate_distance(coord):
    #distance = int((coord[0]**2 + coord[1]**2)**0.5)
    distance = int(math.sqrt(coord[0]**2 + coord[1]**2))
    return distance

def is_target_attackable(distance):
    if distance < config.THRESHOLD:
        return True
    else:
        return False

if __name__ == "__main__":
    coord = (2,1)
    distance = calculate_distance(coord)
    can_attack = is_target_attackable(distance)
    if can_attack:
        print("可击打")
    else:
        print("不可击打")
