# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
x = y = 0
d = s ** 2 - 4 * p
if d < 0:
    print('Задача не решаема')
elif d == 0:
    x = (s + d ** 0.5) / 2
    print(f'Первое число: {int(x)}, второе число: {int(x)}')
else:
    x = (s + d ** 0.5) / 2
    y = (s - d ** 0.5) / 2
    print(f'Первое число: {int(x)}, второе число: {int(y)}')