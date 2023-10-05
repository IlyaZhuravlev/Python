def check_barcode(barcode):
    a = 0
    b = 0

    for i in range(0, len(barcode), 2):
        a += int(barcode[i])

    for i in range(1, len(barcode), 2):
        b += 3 * int(barcode[i])
    
    c = a + b

    if b % 10 == 0:
        return "yes"
    else:
        return "no"

input_barcode = input("Введите штрих-код: ")
result = check_barcode(input_barcode)
print(result)
