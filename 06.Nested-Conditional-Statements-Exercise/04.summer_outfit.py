degrees = int(input())
day_time = input()

outfit = None
shoes = None

if degrees >= 10 and degrees <=18:
    if day_time == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif day_time == 'Afternoon' or 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif degrees > 18 and degrees <= 24:
    if day_time == 'Morning' or day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif day_time == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif degrees >= 25:
    if day_time == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif day_time == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    elif day_time == 'Evening':
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')