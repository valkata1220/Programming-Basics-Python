number = int(input())

if number >= 1 and number <= 7:
    if number == 1:
        print('Monday')
    elif number == 2:
        print('Tuesday')
    elif number == 3:
        print('Wednesday')
    elif number == 4:
        print('Thursday')
    elif number == 5:
        print('Friday')
    elif number == 6:
        print('Saturday')
    else:
        print('Sunday')
else:
    print('Error')
