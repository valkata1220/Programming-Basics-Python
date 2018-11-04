city = input()
sales_volume = float(input())
commission = -1
if (city == 'Sofia' or city == 'Varna' or city == 'Plovdiv') and sales_volume >= 0:
    if city == 'Sofia':
        if sales_volume <= 500:
            commission = 0.05
        elif sales_volume <= 1000:
            commission = 0.07
        elif sales_volume <= 10000:
            commission = 0.08
        else:
            commission = 0.12
    elif city == 'Varna':
        if sales_volume <= 500:
            commission = 0.045
        elif sales_volume <= 1000:
            commission = 0.075
        elif sales_volume <= 10000:
            commission = 0.10
        else:
            commission = 0.13
    else:
        if sales_volume <= 500:
            commission = 0.055
        elif sales_volume <= 1000:
            commission = 0.08
        elif sales_volume <= 10000:
            commission = 0.12
        else:
            commission = 0.145
else:
    print('error')

if commission <= 0:
    print('error')
else:
    print(f'{sales_volume * commission:.2f}')