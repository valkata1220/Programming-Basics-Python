exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
hour = None
minutes = None

exam_in_minutes = exam_hour * 60 + exam_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes

minutes_late = arrival_in_minutes - exam_in_minutes
minutes_early = exam_in_minutes - arrival_in_minutes

if minutes_late > 0 and minutes_late <= 59:
    print('Late')
    print(f'{minutes_late} minutes after the start')
elif minutes_late >= 60:
    hour = minutes_late // 60
    minutes = minutes_late % 60
    print('Late')
    print(f'{hour}:{minutes:02d} hours after the start')
elif minutes_early == 0:
    print('on time')
elif minutes_early <= 30 and minutes_early > 0:
    print('on time')
    print(f'{minutes_early} minutes before the start')
elif minutes_early > 30 and minutes_early <= 59:
    print('Early')
    print(f'{minutes_early} minutes before the start')
elif minutes_early >= 60:
    hour = minutes_early // 60
    minutes = minutes_early % 60
    print('Early')
    print(f'{hour}:{minutes:02d} hours before the start')