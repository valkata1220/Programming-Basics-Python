pairs_count = int(input())

max_differnce = 0
previous_sum = 0
current_sum = 0

for i in range(pairs_count):
    current_sum = 0
    if i == 0:
        previous_sum += int(input())
        previous_sum += int(input())
    else:
        current_sum += int(input())
        current_sum += int(input())

        if abs(previous_sum - current_sum) > max_differnce:
            max_differnce = abs(previous_sum - current_sum)
        previous_sum = current_sum

if max_differnce == 0:
    print(f'Yes, value={previous_sum}')
else:
    print(f'No, maxdiff={max_differnce}')