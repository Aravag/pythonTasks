vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
text = input()
listText = list(text.lower())
finalList = []
for vowel in vowels:
    count = 0
    for letter in listText:
        if letter == vowel:
            count += 1
        elif letter == ' ':
            if count != 0:
                finalList.append(count)
            count = 0
    if count != 0:
        finalList.append(count)
if len(set(finalList)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')