# Задание было в изначальном дз. Но теперь, как дополнительное идет. Найти сумму цифр вещественного числа (и не только)
num = input('Введите вещественное число: ')
sum = 0
listNum = list(num)
sum = 0
for i in range(len(listNum)):
    if listNum[i] == '-' or listNum[i] == '.':
        continue
    else:
        listNum[i] = int(listNum[i])
        sum += listNum[i]
if float(num) < 0:
    print(-sum)
else:
    print(sum)

# Ниже попытка, не увенчавшаяся успехом, но может укажешь на ошибки :)

# if num != int(num):
#     while num != int(num):
#         num *= 1000
# while num != 0:
#     sum += num % 10
#     num //= 10
# print(int(sum))