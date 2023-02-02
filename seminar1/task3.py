num=input('Введите номер билета: ')
if len(num) > 6 or len(num) < 6:
    print('Некорректный номер билета.')
else:
    num = abs(int(num))
    if num // 100000 + num // 10000 % 10 + num // 1000 % 10 == num // 100 % 10 + num // 10 % 10 + num % 10:
        print("yes")
    else: 
        print("no")