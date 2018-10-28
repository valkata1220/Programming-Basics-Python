mm = 1000
cm = 100
mi = 0.000621371192
inches = 39.3700787
km = 0.001
ft = 3.2808399
yd = 1.0936133

number = float(input())
unit_from = input()
unit_to = input()
meters = number
result = 0

if unit_from == 'mm':
    meters = number / mm
elif unit_from == 'cm':
    meters = number / cm
elif unit_from == 'mi':
    meters = number / mi
elif unit_from == 'in':
    meters = number / inches
elif unit_from == 'km':
    meters = number / km
elif unit_from == 'ft':
    meters = number / ft
elif unit_from == 'yd':
    meters = number / yd

if unit_to == 'mm':
    result = meters * mm
elif unit_to == 'cm':
    result = meters * cm
elif unit_to == 'mi':
    result = meters * mi
elif unit_to == 'in':
    result = meters * inches
elif unit_to == 'km':
    result = meters * km
elif unit_to == 'ft':
    result = meters * ft
elif unit_to == 'yd':
    result = meters * yd
elif unit_to == 'm':
    result = meters

print(f'{result:.8f}')
