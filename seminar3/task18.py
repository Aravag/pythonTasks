import random
numLen = int(input('Введите длинну массива: '))
numFind = int(input('Введите число для поиска: '))
numArr = [random.randint(0, 10) for i in range(numLen)]
finalNum = 0
print(numArr)
for i in numArr:
    if numFind - i < numFind - finalNum and numFind - i > 0 or numFind == i:
        finalNum = i
print(finalNum)