a = abs(int(input()))
b = abs(int(input()))
c = abs(int(input()))
if c < a * b and (c % b == 0 or c % a == 0):
    print('yes')
else:
    print('no')