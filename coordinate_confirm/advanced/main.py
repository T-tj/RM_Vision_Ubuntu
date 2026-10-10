from coordinate_confirm.advanced.models import aiming as am
def main():
    center = (150,100)
    targets = [
    (210, 60),
        (90, 140),
        (150, 100),
        (160, 90),
        (161, 89)
]
    total_num = 0
    near_num = 0
    for target in targets:
        total_num += 1
        offset = am.calculate_offset(target,center)
        direction = am.decide_direction(offset)
        is_near = am.is_near_center(offset)

        if is_near:
            near_num += 1

        print(f"目标：{target} | 偏差：{offset} | {direction[0]},{direction[1]} | 中心附近：{is_near}")
    print(f"本次处理 {total_num} 个目标,其中 {near_num} 个位于中心附近。")


if __name__ == "__main__":
    main()