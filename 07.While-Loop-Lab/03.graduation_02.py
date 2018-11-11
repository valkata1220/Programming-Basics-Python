name = input()

grade_count = 1
sum_grades = 0.0
excluded_times = 0

while grade_count <= 12 and excluded_times < 2:
    grade = float(input())

    if grade < 4:
        excluded_times += 1
    else:
        grade_count += 1
        sum_grades += grade

if excluded_times < 2:
    print(f'{name} graduated. Average grade: {(sum_grades / 12):.2f}')
else:
    print(f'{name} has been excluded at {grade_count} grade')