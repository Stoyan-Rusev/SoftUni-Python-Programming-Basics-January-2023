start_number = int(input())
end_number = int(input())

counter = 1
odd_sum = 0
even_sum = 0

for number in range(start_number, end_number + 1):
    for ch in str(number):

        if counter % 2 != 0:
            odd_sum += int(ch)
        elif counter % 2 == 0:
            even_sum += int(ch)

        counter += 1

    if odd_sum == even_sum:
        print(number, end=' ')

    counter = 1
    odd_sum = 0
    even_sum = 0
