fruit = input().lower()
day = input().lower()
quantity = float(input())

if day == 'monday' or day == 'tuesday' or day == 'wednesday' or day == 'thursday' or day == 'friday':
    if fruit == 'banana':
        print(f'{quantity * 2.50:.2f}')
    elif fruit == 'apple':
        print(f'{quantity * 1.20:.2f}')
    elif fruit == 'orange':
        print(f'{quantity * 0.85:.2f}')
    elif fruit == 'grapefruit':
        print(f'{quantity * 1.45:.2f}')
    elif fruit == 'kiwi':
        print(f'{quantity * 2.70:.2f}')
    elif fruit == 'pineapple':
        print(f'{quantity * 5.50:.2f}')
    elif fruit == 'grapes':
        print(f'{quantity * 3.85:.2f}')
    else:
        print('error')
elif day == 'saturday' or day == 'sunday':
    if fruit == 'banana':
        print(f'{quantity * 2.70:.2f}')
    elif fruit == 'apple':
        print(f'{quantity * 1.25:.2f}')
    elif fruit == 'orange':
        print(f'{quantity * 0.90:.2f}')
    elif fruit == 'grapefruit':
        print(f'{quantity * 1.60:.2f}')
    elif fruit == 'kiwi':
        print(f'{quantity * 3.00:.2f}')
    elif fruit == 'pineapple':
        print(f'{quantity * 5.60:.2f}')
    elif fruit == 'grapes':
        print(f'{quantity * 4.20:.2f}')
    else:
        print('error')
else:
    print('error')