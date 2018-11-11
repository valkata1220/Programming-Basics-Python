glass_volume = int(input())
button_pressed_count = 0

while(glass_volume > 0):
    button_pressure = input()
    if button_pressure == 'Easy':
        glass_volume -= 50
    elif button_pressure == 'Medium':
        glass_volume -= 100
    elif button_pressure == 'Hard':
        glass_volume -= 200
    button_pressed_count += 1

if glass_volume == 0:
    print(f'The dispenser has been tapped {button_pressed_count} times.')
else:
    print(f'{abs(glass_volume)}ml has been spilled.')