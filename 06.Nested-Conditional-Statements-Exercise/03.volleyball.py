import math

year = input()
holiday = int(input())
weekends = int(input())

year_holidays = 48
weekends_in_sofia = 48 - weekends
vladi_weekends = weekends_in_sofia * 0.75
holiday_days = holiday * (2/3)

total_games = vladi_weekends + weekends + holiday_days

if year == 'leap':
   total_games *= 1.15

print(f'{math.floor(total_games)}')