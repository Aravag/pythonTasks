count = int(input('Введите количество: '))
#  1
# 4 2
#  3
berries = []
sum = []
i = 0
print('Введите ягоды: ')
for i in range(count) :
    berries.append(int(input())) 
for i in range(count):
    if i == 0:
        sum.append(berries[count-1] + berries[i] + berries[i+1])
    elif i != count - 1:
        sum.append(berries[i-1] + berries[i] + berries[i+1])
    else:
        sum.append(berries[i-1] + berries[i] + berries[0])
print('Наибольшее число равняется '+str(max(sum)))