min_barcode = int(input())
max_barcode = int(input())

for barcode in range(min_barcode, max_barcode + 1):
    pin = ""

    for index, digit in enumerate(str(barcode)):

        if index == 0:
            if int(digit) % 2 == 0:
                break
            else:
                pin += f"{digit}"

        elif index == 1:
            if int(digit) % 2 == 0:
                break
            else:
                pin += f"{digit}"

        elif index == 2:
            if int(digit) % 2 == 0:
                break
            else:
                pin += f"{digit}"

        elif index == 3:
            if int(digit) % 2 == 0:
                break
            else:
                pin += f"{digit}"
                print(pin, end=" ")
