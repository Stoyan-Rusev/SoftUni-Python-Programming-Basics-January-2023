cake_pieces = int(input()) * int(input())

while cake_pieces > 0:
    pieces_taken = input()

    if pieces_taken == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break

    cake_pieces -= int(pieces_taken)

else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
