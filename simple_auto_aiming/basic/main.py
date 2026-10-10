from models import detector as det
from models import geometry as geo
from models import utils 
def main():
    coord = det.detect()
    distance = geo.calculate_distance(coord)
    can_attack = geo.is_target_attackable(distance)
    utils.log(coord,distance,can_attack)

if __name__ == "__main__":
    main()
