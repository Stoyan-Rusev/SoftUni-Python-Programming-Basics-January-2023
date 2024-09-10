total_tickets_count = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie_name = input()
    if movie_name == "Finish":
        break

    free_seats = int(input())
    seats_taken = 0

    while True:
        ticket_type = input()
        if ticket_type == "End":
            print(f"{movie_name} - {seats_taken / free_seats * 100:.2f}% full.")
            break

        if ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        seats_taken += 1
        total_tickets_count += 1

        if seats_taken == free_seats:
            print(f"{movie_name} - 100% full.")
            break

print(f"Total tickets: {total_tickets_count}")
print(f"{student_tickets / total_tickets_count * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets_count * 100:.2f}% standard tickets.")
print(f"{kid_tickets / total_tickets_count * 100:.2f}% kid tickets.")
