import time
from models import detector as det
from models import geometry as geo
from models import utils 
def main():
    while True:
        print("\033[H\033[J",end="")
        coords = det.detect()
        distances = geo.calculate_distances(coords)
        closest = geo.get_closest_distance(distances)
        can_attack = geo.is_target_attackable(closest)
        utils.log(coords,distances,closest,can_attack)

        time.sleep(1)

if __name__ == "__main__":
    main()
