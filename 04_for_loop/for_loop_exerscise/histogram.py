n = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

total = p1 + p2 + p3 + p4 + p5

print(f'{p1 / total * 100:.2f}%')
print(f'{p2 / total * 100:.2f}%')
print(f'{p3 / total * 100:.2f}%')
print(f'{p4 / total * 100:.2f}%')
print(f'{p5 / total * 100:.2f}%')


