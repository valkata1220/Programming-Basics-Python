numbers_count = int(input())

oddSum = 0
oddMin = 'No'
oddMax = 'No'

evenSum = 0
evenMin = 'No'
evenMax = 'No'

current_number = None

for i in range(numbers_count):
    current_number = float(input())
    if i % 2:
        if evenMin == 'No':
            evenMin = current_number
            evenMax = current_number
        if current_number > evenMax:
            evenMax = current_number
        if current_number < evenMin:
            evenMin = current_number
        evenSum += current_number
    else:
        if oddMin == 'No':
            oddMin = current_number
            oddMax = current_number
        if current_number > oddMax:
            oddMax = current_number
        if current_number < oddMin:
            oddMin = current_number
        oddSum += current_number

print(f'OddSum={oddSum:g}')
if oddMin == 'No':
    print(f'OddMin={oddMin}')
    print(f'OddMax={oddMax}')
else:
    print(f'OddMin={oddMin:g}')
    print(f'OddMax={oddMax:g}')

print(f'EvenSum={evenSum:g}')
if evenMin == 'No':
    print(f'EvenMin={evenMin}')
    print(f'EvenMax={evenMax}')
else:
    print(f'EvenMin={evenMin:g}')
    print(f'EvenMax={evenMax:g}')

