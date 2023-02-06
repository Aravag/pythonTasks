import random
numLen = int(input('Введите длинну массива: '))
numFind = int(input('Введите число для поиска: '))
numArr = [random.randint(0, 10) for i in range(numLen)]
count = 0
print(numArr)
for i in numArr:
    if numFind == i:
        count += 1
if count == 0:
    print('Введенного числа нет в массиве.')
elif count == 2 or count == 3 or count == 4:
    print(f'Введенное число встретилось {count} раза.')
else:
    print(f'Введенное число встретилось {count} раз.')