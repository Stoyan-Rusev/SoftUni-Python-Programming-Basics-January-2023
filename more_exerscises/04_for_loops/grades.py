students_count = int(input())

top_students = 0
between_four_five = 0
between_three_four = 0
between_two_three = 0
total_sum_of_grades = 0

for i in range(1, students_count + 1):
    grade = float(input())

    if grade >= 5:
        top_students += 1
    elif grade >= 4:
        between_four_five += 1
    elif grade >= 3:
        between_three_four += 1
    elif grade >= 2:
        between_two_three += 1

    total_sum_of_grades += grade

average = total_sum_of_grades / students_count

print(f"Top students: {top_students / students_count * 100:.2f}%")
print(f"Between 4.00 and 4.99: {between_four_five / students_count * 100:.2f}%")
print(f"Between 3.00 and 3.99: {between_three_four / students_count * 100:.2f}%")
print(f"Fail: {between_two_three / students_count * 100:.2f}%")
print(f"Average: {average:.2f}")
