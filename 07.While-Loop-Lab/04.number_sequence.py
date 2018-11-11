max = int(input())
min = max

input_line = input()

while not(input_line == 'END'):
    current_number = int(input_line)
    if max < current_number:
        max = current_number
    if min > current_number:
        min = current_number
    input_line = input()

print(f'Max number: {max}')
print(f'Min number: {min}')