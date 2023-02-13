n = int(input('Введите число n: '))
m = int(input('Введите число m: '))
listN = []
listM = []
listFin = []
print('Введите числа N: ')
for i in range(n):
    listN.append(int(input()))
print('Введите числа M: ')
for i in range(m):
    listM.append(int(input()))
# Первый вариант перебора списков

# for element in listM:
#     if element in listN:
#         listFin.append(element)

# Второй вариант перебора списков

# listFin.append([x for x in listN if x in listM])

listFin = set(listN) & set(listM)
print(sorted(listFin))