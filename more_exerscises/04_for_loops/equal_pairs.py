from sys import maxsize
amount_of_pairs = int(input())

previous_pair = int(input()) + int(input())
equal_pairs = 0
max_diff = -maxsize

for i in range(2, amount_of_pairs + 1):
    pair = int(input()) + int(input())

    if pair == previous_pair:
        equal_pairs += 1

    if abs(pair - previous_pair) > max_diff:
        max_diff = abs(pair - previous_pair)

    previous_pair = pair

if equal_pairs == amount_of_pairs - 1:
    print(f"Yes, value={previous_pair}")

else:
    print(f"No, maxdiff={max_diff}")
