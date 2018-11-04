n_1 = int(input())
n_2 = int(input())
operator = input()
result = None
even_odd = 'even'

if operator == '+':
    result = n_1 + n_2
    if result % 2:
        even_odd = 'odd'
    print(f'{n_1} + {n_2} = {result} - {even_odd}')
elif operator == '-':
    result = n_1 - n_2
    if result % 2:
        even_odd = 'odd'
    print(f'{n_1} - {n_2} = {result} - {even_odd}')
elif operator == '*':
    result = n_1 * n_2
    if result % 2:
        even_odd = 'odd'
    print(f'{n_1} * {n_2} = {result} - {even_odd}')
elif operator == '/':
    if n_2 == 0:
        print(f'Cannot divide {n_1} by zero')
    else:
        print(f'{n_1} / {n_2} = {n_1/n_2:.2f}')
elif operator == '%':
    if n_2 == 0:
        print(f'Cannot divide {n_1} by zero')
    else:
        print(f'{n_1} % {n_2} = {n_1%n_2}')
