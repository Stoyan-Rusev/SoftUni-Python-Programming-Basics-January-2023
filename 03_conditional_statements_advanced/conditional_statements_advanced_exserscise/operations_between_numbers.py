n = int(input())
n_2 = int(input())
operator = input()

result = None

if operator == "+":
    result = f"{n} {operator} {n_2} = {n + n_2}"
    if (n + n_2) % 2 == 0:
        result += " - even"
    else:
        result += " - odd"


elif operator == "-":
    result = f"{n} {operator} {n_2} = {n - n_2}"
    if n - n_2 % 2 == 0:
        result += " - even"
    else:
        result += " - odd"

elif operator == "*":
    result = f"{n} {operator} {n_2} = {n * n_2}"
    if n * n_2 % 2 == 0:
        result += " - even"
    else:
        result += " - odd"

elif n_2 == 0:
    result = f"Cannot divide {n} by zero"

elif operator == "/":
    result = f"{n} / {n_2} = {n / n_2:.2f}"

elif operator == "%":
    result = f"{n} % {n_2} = {n % n_2}"

print(result)
