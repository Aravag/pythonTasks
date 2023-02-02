# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.
num = abs(int(input('Введите число: ')))
numList = []
i = 0
sqrtNum = 0
while sqrtNum < num:
    sqrtNum = 2 ** i
    numList.append(sqrtNum)
    i += 1 
if numList[-1] > num:
    numList.pop()
print(numList)