numbers_count = int(input())

even_sum = 0
odd_sum = 0

for i in range(numbers_count):
    if i % 2:
        odd_sum += int(input())
    else:
        even_sum += int(input())

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')