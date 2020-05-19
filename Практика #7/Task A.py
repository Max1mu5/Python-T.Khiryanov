car_weight = int(input())
car_plat_height = int(input())

piano_exist = True
piano_weight = int(input())
piano_height = int(input())

frig_exist = True
frig_weight = int(input())
frig_height = int(input())

bridge_max_weight = int(input()) - car_weight
tunnel_max_height = int(input()) - car_plat_height

#   -> bridge -> inst
#   |
# --|
#   |
#   -> tunnel -> inst_home

if piano_height > frig_height:
    max_height = piano_height
else:
    max_height = frig_height


if max_height <= tunnel_max_height:
    frig_exist = False
else:
    if frig_weight + piano_weight <= bridge_max_weight:
        piano_exist = False

if piano_exist:
    if piano_weight <= bridge_max_weight:
        piano_exist = False
elif frig_exist:
    if frig_height <= tunnel_max_height:
        frig_exist = False

if (not piano_exist) and (not frig_exist):
    print('YES')
else:
    print("NO")


