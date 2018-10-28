import math

income = float(input())
average_grade = float(input())
minimum_wage = float(input())

social_scholarship = 0
excellent_grades_scholarship = 0
if income < minimum_wage and average_grade > 4.50:
    social_scholarship = minimum_wage * 0.35

if average_grade >= 5.5:
    excellent_grades_scholarship = average_grade * 25

if social_scholarship == 0 and excellent_grades_scholarship == 0:
    print(f'You cannot get a scholarship!')
elif social_scholarship > excellent_grades_scholarship:
    print(f'You get a Social scholarship {math.floor(social_scholarship)} BGN')
else:
    print(f'You get a scholarship for excellent results {math.floor(excellent_grades_scholarship)} BGN')