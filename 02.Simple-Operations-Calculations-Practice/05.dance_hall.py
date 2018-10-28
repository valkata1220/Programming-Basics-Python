import math

l = float(input())
w = float(input())
wardrobe_side = float(input())

room_size = (l * 100.0) * (w * 100.0)
wardrobe = (wardrobe_side * 100.0) * (wardrobe_side * 100.0)
bench = room_size / 10

free_space = room_size - wardrobe - bench
dancers = free_space / (40+7000)
print(f'{math.floor(dancers)}')