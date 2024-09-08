exam_hour = int(input()) * 60
exam_minute = int(input())
arrival_hour = int(input()) * 60
arrival_minute = int(input())

exam_time = exam_hour + exam_minute
arrival_time = arrival_hour + arrival_minute

if arrival_time > exam_time:
    print("Late")
    if (arrival_time - exam_time) < 60:
        print(f"{arrival_time - exam_time} minutes after the start")
    else:
        print(f"{(arrival_time - exam_time) // 60}:{(arrival_time - exam_time) % 60:02d} hours after the start")

elif arrival_time < exam_time - 30:
    print("Early")
    if exam_time - arrival_time < 60:
        print(f"{exam_time - arrival_time} minutes before the start")
    else:
        print(f"{(exam_time - arrival_time) // 60}:{(exam_time - arrival_time) % 60:02d} hours before the start")

else:
    if arrival_time == exam_time:
        print("On time")
    else:
        print("On time")
        print(f"{exam_time - arrival_time} minutes before the start")






