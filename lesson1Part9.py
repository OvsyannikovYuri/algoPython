# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).


a = int(input("введите 1ое число"))
b = int(input("введите 2ое число"))
c = int(input("введите 3ое число"))
mini = 0
maxi = 0
if (a > b):
    if (a > c):
        maxi = a
    elif (c > a & c > b):
        maxi = c
    else:
        maxi = b

if (a < b):
    if (a < c):
        mini = a
    elif (c < b & c < a):
        mini = c
    else:
        mini = b
spisok = [a,b,c]
minmax = [mini,maxi]
print (minmax)




