numbers_count = int(input())

min_number = int(input())
current_number = None

for i in range(numbers_count - 1):
    current_number = int(input())
    if current_number < min_number:
        min_number = current_number

print(min_number)