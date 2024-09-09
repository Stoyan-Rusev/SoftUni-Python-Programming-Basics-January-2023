name = input()

years_completed = 0
times_failed = 0
total_grades_sum = 0


while True:
    grade = float(input())

    if grade >= 4:
        total_grades_sum += grade
        years_completed += 1

        if years_completed == 12:
            print(f"{name} graduated. Average grade: {total_grades_sum / 12:.2f}")
            break

    else:
        times_failed += 1

        if times_failed == 2:
            print(f"{name} has been excluded at {years_completed + 1} grade")
            break

