# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки 
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, 
# которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
from random import randint
countCoin = int(input('Введите количество монет: '))
coinsList = []
i = 0
min = 0
zeroCoin = 0
oneCoin = 0
while i < countCoin:
    coinsList.append(randint(0, 1))
    if coinsList[i] == 0:
        zeroCoin += 1
    else:
        oneCoin += 1
    i += 1
if zeroCoin > oneCoin:
    min = oneCoin
else:
    min = zeroCoin
print(coinsList)
print(min)