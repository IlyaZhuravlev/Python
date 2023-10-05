def count_b_and_a(string):
    b = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    b_count = 0
    a_count = 0

    for char in string.lower():
        if char.isalpha() and char != ' ':
            if char in b:
                b_count += 1
            else:
                a_count += 1

    return b_count, a_count
input_string = input("Введите строку: ")
b, a = count_b_and_a(input_string)
print(f" гласных: {b}", f" согласных: {a}" )
