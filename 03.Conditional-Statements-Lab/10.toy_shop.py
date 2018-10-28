excursion_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

puzzle_price = 2.60
doll_price = 3.0
bear_price = 4.10
minion_price = 8.20
truck_price = 2.0

toys_price = (puzzle_count * puzzle_price) + (doll_count * doll_price) + \
             (bear_count * bear_price) + (minion_count * minion_price) + (truck_count * truck_price)

toys_count = puzzle_count + doll_count + bear_count + minion_count + truck_count


if toys_count >= 50:
    toys_price -= toys_price * 25 / 100

toys_price -= (toys_price * 10 / 100)

difference = toys_price - excursion_price;

if difference < 0:
    print(f'Not enough money! {abs(difference):.2f} lv needed.')
else:
    print(f'Yes! {difference:.2f} lv left.')