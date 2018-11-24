open_tabs_count = int(input())
salary = int(input())

facebook = 150
instagram = 100
reddit = 50
current_tab = None

for i in range(open_tabs_count):
    current_tab = input()

    if current_tab == 'Facebook':
        salary -= facebook
    elif current_tab == 'Instagram':
        salary -= instagram
    elif current_tab == 'Reddit':
        salary -= reddit

    if salary <= 0:
        break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
