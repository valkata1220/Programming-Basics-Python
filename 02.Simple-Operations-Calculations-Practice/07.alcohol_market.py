whiskey_price = float(input())
beer_liters = float(input())
wine_liters = float(input())
rakia_liters = float(input())
whiskey_liters = float(input())

rakia_price = whiskey_price / 2
wine_price = rakia_price - (rakia_price * 0.4)
beer_price = rakia_price - (rakia_price * 0.8)

rakia_total = rakia_price * rakia_liters
wine_total = wine_price * wine_liters
beer_total = beer_price * beer_liters
whiskey_total = whiskey_price * whiskey_liters

total_sum = rakia_total + wine_total + beer_total + whiskey_total

print(f'{total_sum:.2f}')