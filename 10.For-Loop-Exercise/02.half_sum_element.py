numbers_count = int(input())
max_number = int(input())
sum = max_number
current_number = None

for i in range(1,numbers_count):
    current_number = int(input())
    if max_number < current_number:
        max_number = current_number
    sum += current_number

sum -= max_number

if sum == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(max_number - sum)}')
    