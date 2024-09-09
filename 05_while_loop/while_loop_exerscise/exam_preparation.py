maximum_amount_bad_grades = int(input())

bad_grades = 0
average_score = 0
amount_tasks = 0
sum_grades = 0
last_task = None

while True:
    task = input()

    if task == "Enough":
        print(f"Average score: {average_score:.2f}")
        print(f"Number of problems: {amount_tasks}")
        print(f"Last problem: {last_task}")
        break

    grade = int(input())

    if grade < 5:
        bad_grades += 1

    if bad_grades == maximum_amount_bad_grades:
        print(f"You need a break, {bad_grades} poor grades.")
        break

    sum_grades += grade
    amount_tasks += 1
    last_task = task
    average_score = sum_grades / amount_tasks
