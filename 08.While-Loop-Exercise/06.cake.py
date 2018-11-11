cake_width = int(input())
cake_length = int(input())

cake_size = cake_width * cake_length


while cake_size >= 0:
    input_line = input()
    if input_line == 'STOP':
        break
    pieces = int(input_line)
    cake_size -= pieces

if cake_size < 0:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')
else:
    print(f'{cake_size} pieces are left.')