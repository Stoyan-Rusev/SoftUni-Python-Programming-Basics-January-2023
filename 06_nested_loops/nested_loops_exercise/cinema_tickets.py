student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie = input()
    if movie == "Finish":
        break

    capacity = int(input())

    sold_tickets = 0

    while sold_tickets < capacity:
        ticket_type = input()

        if ticket_type == "End":
            break
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        sold_tickets += 1

    print(f"{movie} - {sold_tickets / capacity * 100:.2f}% full.")

total_tickets = standard_tickets + student_tickets + kid_tickets

print(f"Total tickets: {total_tickets}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets * 100:.2f}% kids tickets.")
