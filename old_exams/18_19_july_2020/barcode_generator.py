min_barcode = int(input())
max_barcode = int(input())

for barcode in range(min_barcode, max_barcode + 1):
    for digit in str(barcode):
        if int(digit) % 2 == 0:
            break
        

