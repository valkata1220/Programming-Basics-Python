dissatisfied_mark = int(input())

bad_marks = 0
total_sum = 0
last_problem = None
problems_count = 0

while True:
    task = input()

    if task == 'Enough':
        print(f'Average score: {total_sum / problems_count:.2f}')
        print(f'Number of problems: {problems_count}')
        print(f'Last problem: {last_problem}')
        break
    else:
        last_problem = task
        problems_count += 1
        mark = int(input())
        total_sum += mark
        if mark <= 4:
            bad_marks += 1
    if dissatisfied_mark == bad_marks:
        print(f'You need a break, {dissatisfied_mark} poor grades.')
        break



