from models import config as con
import math
def calculate_distances(coords):
    distances = []
    for coord in coords:
        distance = int (math.sqrt(coord[0]**2 + coord[1]**2))
        distances.append(distance)
    return distances

def get_closest_distance(distances):
    if not distances:   #空列表【】被视为假，此时not distances为真，执行if
        return None
    return min(distances)

def is_target_attackable(closest):
    if closest is None:  #若让None与距离阈值比较，运行会报错，所以提前拦截
        return False
    return closest < con.THRESHOLD
    