from coordinate_confirm.basic.models import aiming as am

center = (150,100)
target = (210,60)
offset_x = am.calculate_offset_x(target,center)
direction = am.decide_horizontal(offset_x)
print(f"当前目标: {target}, 横向偏差: ({offset_x}), 建议: {direction}")