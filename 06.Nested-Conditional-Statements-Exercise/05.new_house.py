flower_type = input()
flowers_count = int(input())
budget = int(input())

total_price = None

if flower_type == 'Roses':
    total_price = flowers_count * 5
    if flowers_count > 80:
        total_price -= total_price * 0.10
elif flower_type == 'Dahlias':
    total_price = flowers_count * 3.80
    if flowers_count > 90:
        total_price -= total_price *  0.15
elif flower_type == 'Tulips':
    total_price = flowers_count * 2.80
    if flowers_count > 80:
        total_price -= total_price * 0.15
elif flower_type == 'Narcissus':
    total_price = flowers_count * 3
    if flowers_count < 120:
        total_price += total_price * 0.15
elif flower_type == 'Gladiolus':
    total_price = flowers_count * 2.50
    if flowers_count < 80:
        total_price += total_price * 0.20


money = budget - total_price

if money < 0:
    print(f'Not enough money, you need {abs(money):.2f} leva more.')
else:
    print(f'Hey, you have a great garden with {flowers_count} {flower_type} and {money:.2f} leva left.')