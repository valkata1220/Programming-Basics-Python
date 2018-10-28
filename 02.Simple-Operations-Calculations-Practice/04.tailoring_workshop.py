table_count = int(input())
table_length = float(input())
table_width = float(input())

table_cover_area = table_count * (table_length + 2 * 0.30) * (table_width + 2 * 0.30)
square_pattern = table_count * (table_length / 2) * (table_length / 2)

price_usd = (table_cover_area * 7) + (square_pattern * 9)
price_bgn = price_usd * 1.85

print(f'{price_usd:.2f} USD')
print(f'{price_bgn:.2f} BGN')
