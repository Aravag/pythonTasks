from random import randint

def findIndex(num1, num2, list, listIndex):
    i = 0
    while i < len(list):
        if num1 <= list[i] <= num2:
            listIndex.append(i)
        i += 1
    return listIndex

num1 = int(input('Введите число начала: '))
num2 = int(input('Введите число конца: '))

listNum = [randint(-20, 20) for i in range(15)]
listIndex = []

print(listNum)

findIndex(num1, num2, listNum, listIndex)
print(f'Индексы подходящих чисел: {listIndex}')