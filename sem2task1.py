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

# Ниже две попытки, не увенчавшиеся успехом, но может укажешь на ошибки :)

# if num != int(num):
#     while num != int(num):
#         num *= 1000
# while num != 0:
#     sum += num % 10
#     num //= 10
# print(int(sum))

# for i in range(len(str(num))):
#     if str(num)[i].isdigit == False:
#         continue
#     else:
#         sum += int(str(num)[i])
# print(int(sum))