numbers_count = int(input())

left_sum = 0
right_sum = 0

for i in range(numbers_count):
    left_sum += int(input())

for i in range(numbers_count):
    right_sum += int(input())

if left_sum == right_sum:
    print(f'Yes, sum = ${right_sum}')
else:
    print(f'No, diff = ${abs(left_sum - right_sum)}')

