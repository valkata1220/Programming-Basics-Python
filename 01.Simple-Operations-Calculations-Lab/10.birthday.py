aquarium_length = float(input())
aquarium_width = float(input())
aquarium_height = float(input())
percent = float(input())

volume = aquarium_length * aquarium_width * aquarium_height
liters = volume * 0.001

percent = percent * 0.01
final_aquarium_water = liters * (1 - percent)

print(f'{final_aquarium_water:.3f}')