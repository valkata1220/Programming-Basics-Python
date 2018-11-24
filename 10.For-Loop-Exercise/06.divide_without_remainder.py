numbers_count = int(input())
p1 = 0
p2 = 0
p3 = 0
current_number = None

for i in range(numbers_count):
    current_number = int(input())

    if current_number % 2 == 0:
        p1 += 1
    if current_number % 3 == 0:
        p2 += 1
    if current_number % 4 == 0:
        p3 += 1

print(f'{p1 / numbers_count * 100:.2f}%')
print(f'{p2 / numbers_count * 100:.2f}%')
print(f'{p3 / numbers_count * 100:.2f}%')