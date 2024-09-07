first_racer_time = int(input())
second_racer_time = int(input())
third_racer_time = int(input())

total_time = first_racer_time + second_racer_time + third_racer_time

minutes = total_time // 60
seconds = total_time % 60

print(f'{minutes}:{seconds:02d}')

