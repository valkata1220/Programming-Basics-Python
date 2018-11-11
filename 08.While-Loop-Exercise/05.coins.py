change = float(input())
coints_count = 0

while change > 0:
    if(change >= 2):
        coints_count += 1
        change -= 2
    elif change >= 1:
        coints_count += 1
        change -= 1
    elif change >= 0.50:
        coints_count += 1
        change -= 0.50
    elif change >= 0.20:
        coints_count += 1
        change -= 0.20
    elif change >= 0.10:
        coints_count += 1
        change -= 0.10
    elif change >= 0.05:
        coints_count += 1
        change -= 0.05
    elif change >= 0.02:
        coints_count += 1
        change -= 0.02
    else:
        coints_count += 1
        change -= 0.01
    change = float(f'{change:.2f}')
print(coints_count)