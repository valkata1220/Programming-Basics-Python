x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x = float(input())
y = float(input())

if x >= x_1 and x <= x_2:
    if y >= y_1 and y <= y_2:
        print('Inside')
    else:
        print('Outside')
else:
    print('Outside')