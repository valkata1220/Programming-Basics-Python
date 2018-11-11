payments_count = int(input())
total = 0

while payments_count > 0:
    money_value = float(input())
    if money_value < 0:
        print(f'Invalid operation!')
        break
    else:
        print(f'Increase: {money_value:.2f}')
        total += money_value
    payments_count -= 1

print(f'Total: {total:.2f}')