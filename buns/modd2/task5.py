def shift_alphavit(i, n):
    alphavit = list('abcdefghijklmnopqrstuvwxyz')
    index = alphavit.index(i)
    shifted_index = (index + n) % len(alphavit) 
    shifted_d = alphavit[shifted_index]
    return shifted_d
d = input("Введите символ латинского алфавита: ")
num = int(input("Введите целое число: "))

shifted_d = shift_alphavit(d, num)
print(f"Смещенный символ: {shifted_d}")
