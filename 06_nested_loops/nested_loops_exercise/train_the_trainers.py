number_of_judges = int(input())

all_presentations_grades = 0
presentations = 0

while True:
    presentation = input()

    if presentation == "Finish":
        break

    grades_sum = 0

    for _ in range(number_of_judges):
        grade = float(input())
        grades_sum += grade

    average_grade = grades_sum / number_of_judges
    all_presentations_grades += average_grade
    presentations += 1

    print(f"{presentation} - {average_grade:.2f}.")

print(f"Student's final assessment is {all_presentations_grades / presentations:.2f}.")
