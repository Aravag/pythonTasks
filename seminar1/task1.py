num = abs(int(input('Введите трехзначное число: ')))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(f'Сумма цифр числа равняется {sum}')