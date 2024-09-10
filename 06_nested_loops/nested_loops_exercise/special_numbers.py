n = int(input())

for spec_num in range(1111, 9999 + 1):
    for digit in str(spec_num):
        if digit == "0":
            break
        if n % int(digit) != 0:
            break
    else:
        print(spec_num, end=" ")
