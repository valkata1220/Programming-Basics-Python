group_budget = int(input())
season = input()
fishermans_count = int(input())

boat_fee = None

if season == 'Spring':
    boat_fee = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_fee = 4200
elif season == 'Winter':
    boat_fee = 2600

if  fishermans_count <= 6:
    boat_fee -= boat_fee * 0.10
elif fishermans_count <=11:
    boat_fee -= boat_fee * 0.15
else:
    boat_fee -= boat_fee * 0.25

if season != 'Autumn' and fishermans_count % 2 == 0:
    boat_fee -= boat_fee * 0.05

money = group_budget - boat_fee

if money < 0:
    print(f'Not enough money! You need {abs(money):.2f} leva.')
else:
    print(f'Yes! You have {money:.2f} leva left.')