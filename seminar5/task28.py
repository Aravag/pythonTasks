def sum(a, b):
    if a == 0:
         return b
    else:
        return sum(a-1, b+1)
        
a = int(input("Введите число: "))
b = int(input("Введите второе число: "))
print("Сумма чисел равна:", sum(a, b))