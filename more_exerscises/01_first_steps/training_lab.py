length = float(input()) * 100
width = float(input()) * 100

tables_per_reel = (width - 100) // 70
tables_per_column = length // 120

total = (tables_per_column * tables_per_reel) - 3

print(total)


