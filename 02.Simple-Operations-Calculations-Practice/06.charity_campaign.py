campaign_days = int(input())
pastry_cooks = int(input())
cake_count = int(input())
wafle_count = int(input())
pancake_count = int(input())

cake_price = cake_count * 45.0
wafle_price = wafle_count * 5.80
pancake_price = pancake_count * 3.20

day_price = (cake_price + wafle_price + pancake_price) * pastry_cooks
total_sum = day_price * campaign_days
raised_money = total_sum - (total_sum / 8)

print(f'{raised_money:.2f}')
