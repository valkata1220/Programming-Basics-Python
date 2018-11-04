budget = float(input())
season = input()

accommodation = None
percentage = None
destination = None

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        percentage = 0.30
        accommodation = 'Camp'
    elif season == 'winter':
        accommodation = 'Hotel'
        percentage = 0.70
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        percentage = 0.40
        accommodation = 'Camp'
    elif season == 'winter':
        accommodation = 'Hotel'
        percentage = 0.80
else:
    destination = 'Europe'
    percentage = 0.90
    accommodation = 'Hotel'

price = budget * percentage

print(f'Somewhere in {destination}')
print(f'{accommodation} - {price:.2f}')