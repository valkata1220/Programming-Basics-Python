import math

first_brother = float(input())
second_brother = float(input())
third_brother = float(input())
father_time = float(input())

total_time = 1 / (1 / first_brother + 1 / second_brother + 1 / third_brother)
total_time += total_time * 0.15

time_left = father_time - total_time

if time_left <= 0:
    time_left = math.fabs(time_left)
    print(f'Cleaning time: {total_time:.2f}')
    print(f'No, there isn\'t a surprise - shortage of time -> {math.ceil(time_left)} hours.')
else:
    print(f'Cleaning time: {total_time:.2f}')
    print(f'Yes, there is a surprise - time left -> {math.floor(time_left)} hours.')