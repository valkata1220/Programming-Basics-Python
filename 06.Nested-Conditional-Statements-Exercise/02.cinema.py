screening = input()
rows = int(input())
cols = int(input())

premiere = 12.00
normal = 7.50
discount = 5.00

total_tickets_price = 0

if screening == 'Premiere':
    total_tickets_price = (rows * cols) * premiere
elif screening == 'Normal':
    total_tickets_price = (rows * cols) * normal
elif screening == 'Discount':
    total_tickets_price = (rows * cols) * discount

print(f'{total_tickets_price:.2f} leva')