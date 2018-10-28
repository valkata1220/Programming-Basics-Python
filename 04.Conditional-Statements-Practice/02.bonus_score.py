points = int(input())
bonus_points = 0

if points > 1000:
    bonus_points = points * 0.10 # * 10 / 100
elif points > 100:
    bonus_points = points * 0.20
else:
    bonus_points = 5

if points % 2 == 0:
    bonus_points += 1 # bonus_points = bonus_points + 1
elif points % 10 == 5:
    bonus_points += 2

print(bonus_points)
print(points + bonus_points)


