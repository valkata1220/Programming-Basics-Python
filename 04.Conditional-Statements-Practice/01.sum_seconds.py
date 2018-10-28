seconds_1 = int(input())
seconds_2 = int(input())
seconds_3 = int(input())

total_seconds = seconds_1 + seconds_2 + seconds_3
minutes = total_seconds // 60
left_seconds = total_seconds % 60

print(f'{minutes}:{left_seconds:02d}')


""""if total_seconds >= 60 and total_seconds <= 119:
    minutes = 1
elif total_seconds >= 120 and total_seconds <= 179:
    minutes = 2

left_seconds = total_seconds - (minutes * 60)

if left_seconds < 10:
    print(f'{minutes}:0{left_seconds}')
else:
    print(f'{minutes}:{left_seconds}')"""