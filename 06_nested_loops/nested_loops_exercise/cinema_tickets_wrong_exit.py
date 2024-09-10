tickets_sold = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0

while True:
    movie = input()
    free_seats = int(input())

    current_movie_sold = 0

    while True:
        ticket_type = input()

        if ticket_type == "End":
            print(f"{movie} - {current_movie_sold / free_seats * 100:.2f}% full.")
            break
        elif ticket_type == "Finish":
            print(f"{movie} - {current_movie_sold / free_seats * 100:.2f}% full.")
            print(f"Total tickets: {tickets_sold}")
            print(f"{student_tickets / tickets_sold * 100:.2f}% student tickets.")
            print(f"{standard_tickets / tickets_sold * 100:.2f}% standard tickets.")
            print(f"{kid_tickets / tickets_sold * 100:.2f}% kids tickets.")
            exit()
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1

        tickets_sold += 1
        current_movie_sold += 1
