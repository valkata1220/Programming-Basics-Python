numbers_count = int(input())

max_number = int(input())
current_number = None

for i in range(numbers_count - 1):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

print(max_number)