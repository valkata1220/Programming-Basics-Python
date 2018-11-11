steps_goal = 10000
going_home = False

while not going_home and steps_goal > 0:
    input_line = input()
    if input_line == 'Going home':
        going_home = True
        input_line = input()
    steps_goal -= int(input_line)

if steps_goal <= 0:
    print(f'Goal reached! Good job!')
else:
    print(f'{steps_goal} more steps to reach goal.')