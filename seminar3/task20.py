dictCount = dict.fromkeys(['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], 1)
dictCount.update(dict.fromkeys(['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'], 2))
dictCount.update(dict.fromkeys(['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'], 3))
dictCount.update(dict.fromkeys(['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'], 4))
dictCount.update(dict.fromkeys(['K', 'Ж', 'З', 'Х', 'Ц', 'Ч'], 5))
dictCount.update(dict.fromkeys(['J', 'X', 'Ш', 'Э', 'Ю'], 8))
dictCount.update(dict.fromkeys(['Q', 'Z', 'Ф', 'Щ', 'Ъ'], 10))
finalCount = []
word = list(input('Введите слово для подсчета очков: ').upper())
for letter in word:
    if letter in dictCount.keys():
        finalCount.append(dictCount[letter])
print(f'Стоимость введенного слова: {sum(finalCount)}.')