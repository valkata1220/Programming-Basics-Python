trip_price = float(input())
money_balance = float(input())
spending_count = 0
days_count = 0

while True:
    operation = input()
    money = float(input())
    if operation == 'spend':
        spending_count += 1
        money_balance -= money
        if money_balance < 0:
            money_balance = 0
    elif operation == 'save':
        money_balance += money
        spending_count = 0


    days_count += 1

    if spending_count == 5:
        print('You can\'t save the money.')
        print(days_count)
        break
    elif money_balance >= trip_price:
        print(f'You saved the money for {days_count} days.')
        break