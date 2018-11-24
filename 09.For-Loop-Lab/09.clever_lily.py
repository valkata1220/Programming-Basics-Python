age = int(input())
washing_machine_price = float(input())
toy_price = float(input())

saved_money = 0.0
toys_count = 0
brother_fee = 0
gift_money = 10

for i in range(1,age+1):
    if i % 2 == 0:
        saved_money += gift_money
        gift_money += 10
        brother_fee += 1
    else:
        toys_count += 1

saved_money -= brother_fee
saved_money += toys_count * toy_price

if saved_money >= washing_machine_price:
    print(f'Yes! {saved_money - washing_machine_price:.2f}')
else:
    print(f'No! {washing_machine_price - saved_money:.2f}')