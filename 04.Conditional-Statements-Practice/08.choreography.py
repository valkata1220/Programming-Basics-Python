import math
steps_count = int(input())
dancers_count = int(input())
days_count = int(input())

steps_per_day = math.ceil(((steps_count /days_count) / steps_count)* 100)
dancers_steps = steps_per_day / dancers_count

if steps_per_day > 13:
    print(f'No, They will not succeed in that goal! Required {dancers_steps:.2f}% steps to be learned per day.')
else:
    print(f'Yes, they will succeed in that goal! {dancers_steps:.2f}%.')
