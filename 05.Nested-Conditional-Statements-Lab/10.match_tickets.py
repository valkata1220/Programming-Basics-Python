budget = float(input())
category = input()
people_count = int(input())

vip = 499.99
normal = 249.99

percentage = 0.0
ticket_price = 0.0
if (people_count > 0) and (people_count < 5):
    percentage = 0.75
elif (people_count > 4) and (people_count < 10):
    percentage = 0.60
elif (people_count > 9) and (people_count < 25):
    percentage = 0.50
elif (people_count > 24) and (people_count < 50):
    percentage = 0.40
elif people_count >= 50:
    percentage = 0.25

if category == 'VIP':
    ticket_price = people_count * vip
elif category == 'Normal':
    ticket_price = people_count * normal

budget -= budget * percentage

money = budget - ticket_price

if money < 0:
    print(f'Not enough money! You need {abs(money):.2f} leva.')
else:
    print(f'Yes! You have {money:.2f} leva left.')
