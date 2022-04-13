exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam = exam_minute + exam_hour * 60
arrival = arrival_minute + arrival_hour * 60
diff = exam - arrival

if diff < 0:
    print('Late')
    diff = abs(diff)
    if arrival != exam:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0 :
            print(f'{hours}:{minutes:02d} hours after the start')
        else:
            print(f'{minutes} minutes after the start')
elif 0 <= diff <= 30:
    print('On time')
    if arrival != exam:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0 :
            print(f'{hours}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')
else:
    print('Early')
    if arrival != exam:
        hours = diff // 60
        minutes = diff % 60
        if hours > 0:
            print(f'{hours}:{minutes:02d} hours before the start')
        else:
            print(f'{minutes} minutes before the start')
