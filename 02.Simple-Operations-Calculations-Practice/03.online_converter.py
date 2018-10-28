amount = float(input())
currency_from = input()
currency_to = input()

usd = 1.79549
eur = 1.95583
gbp = 2.53405
result = 0

if currency_from == "BGN" :
    if currency_to == "USD":
        result = amount / usd
    elif currency_to == "EUR":
        result = amount / eur
    elif currency_to == "GBP":
        result = amount / gbp
elif currency_from == "USD":
    if currency_to == "BGN":
        result = amount * usd
    elif currency_to == "EUR":
        result = (amount * usd) / eur
    elif currency_to == "GBP":
        result = (amount * usd) / gbp
elif currency_from == "EUR":
    if currency_to == "USD":
        result = (amount * eur) / usd
    elif currency_to == "BGN":
        result = amount * eur
    elif currency_to == "GBP":
        result = (amount * eur) / gbp
elif currency_from == "GBP":
    if currency_to == "USD":
        result = (amount * gbp) / usd
    elif currency_to == "EUR":
        result = (amount * gbp) / eur
    elif currency_to == "BGN":
        result = amount * gbp

print(f'{result:.2f} {currency_to}')