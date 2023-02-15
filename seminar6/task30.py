num = str(int(input('Введите начало, разницу и длину без пробелов: ')))
intNum = [int(i) for i in str(num)]
print(intNum)
def arithm(num):
    listN = []
    i = num[0]
    j = 0
    while j < num[2]:
        listN.append(i)
        i+=2
        j+=1
    print(listN)
arithm(intNum)
    