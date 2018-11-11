free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())

free_space_volume = free_space_width * free_space_length * free_space_height

while free_space_volume > 0:
    box_input = input()
    if box_input == 'Done':
        break
    free_space_volume -= int(box_input)

if free_space_volume  < 0:
    print(f'No more free space! You need {abs(free_space_volume)} Cubic meters more.')
else:
    print(f'{free_space_volume} Cubic meters left.')