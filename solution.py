import math

y1 = int(input())
x1 = int(input())
y2 = int(input())
x2 = int(input())

res = 'y'
distance = y2 - y1  # макс разброс по X
isEvenY1 = y1 % 2   # четность Y1
isEvenY2 = y2 % 2   # четность Y2
minX = int(math.fabs(x1 - distance))    # миним значение X
if minX < 1:
    if isEvenY2 == 0:
        minX = 2
    else:
        minX = 1
maxX = (x1 + distance)                  # макс значение X
if maxX > 8:
    if isEvenY2 == 0:
        maxX = 8
    else:
        maxX = 7


def isClrBlack(n, m):   # опр. цвет клетки
    res = 'y'
    if n % 2 == 0:
        if m % 2 != 0:
            res = 'n'
    else:
        if m % 2 == 0:
            res = 'n'
    return res

if distance > 0 and isClrBlack(y1, x1) == 'y' and isClrBlack(y2, x2) == 'y':
    if isEvenY1 != 0:   # нечетные строки
        if isEvenY2 == 0:
            if maxX - minX > 2:     # больше 2х значений
                if (x2 >= minX) and (x2 <= maxX):
                    res = 'y'
                else:
                    res = 'n'
            else:   # меншье двух значений
                if x2 == minX or x2 == maxX:
                    res = 'y'
                else:
                    res = 'n'
        else:
            if maxX - minX > 2:  # больше 2х значений
                if (x2 >= minX) and (x2 <= maxX) or x2 == x1:
                    res = 'y'
                else:
                    res = 'n'
            else:
                if x2 == minX or x2 == maxX:
                    res = 'y'
                else:
                    res = 'n'
    else:               # нечетные строки
        if isEvenY2 == 0:
            if maxX - minX > 2:  # больше 2х значений
                if (x2 >= minX) and (x2 <= maxX) or x2 == x1:
                    res = 'y'
                else:
                    res = 'n'
            else:
                if x2 == minX or x2 == maxX:
                    res = 'y'
                else:
                    res = 'n'
        else:
            if maxX - minX > 2:  # больше 2х значений
                if (x2 >= minX) and (x2 <= maxX):
                    res = 'y'
                else:
                    res = 'n'
            else:
                if x2 == minX or x2 == maxX:
                    res = 'y'
                else:
                    res = 'n'
else:
    res = 'n'

if res == 'y':
    print('YES')
else:
    print('NO')
