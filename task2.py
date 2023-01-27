num = abs(int(input('Введите число журавликов: ')))
guys = num//3//2
girl = num - guys * 2
print(f'Петя и Сережа сделали по {guys}, а Катя {girl}')