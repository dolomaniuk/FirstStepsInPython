empty_set = set('letters')
even_numbers = {0,2,4,6,8}
old_numbers = {'1','3','5','7','9'}

set(['Dsher', 'Dancer', 'Prancer', 'Mason-Dixon'])
set(('Ummaguma', 'Echoes', 'Atom Heart Mother'))
set({'apple':'red', 'orange':'orange', 'cherry':'red'})

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

# for name, contents in drinks.items():
#     if contents & {'vermouth', 'orange juice'}:
#         print(name)

# for name, contents in drinks.items():
#     if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        # print(name)

bruss = drinks['black russian']
wruss = drinks['white russian']
print('1: ', bruss, '\n2: ', wruss)
print('intersection:\t', bruss & wruss)
print('union:\t', bruss | wruss)
print('difference 1 - 2:\t', bruss - wruss)
print('difference 2 - 1:\t', wruss - bruss)
print('symmetric_difference:\t', bruss ^ wruss)
print('is 1 a subset to 2:\t', bruss <= wruss)
print('is 2 a subset to 1:\t', wruss <= bruss)
print('is 1 a superset to 2:\t', bruss >= wruss)
print('is 2 a superset to 1:\t', wruss >= bruss)

# sets
a = {1,2}
b = {2,3}
# Intersection sets. Пересечение множест ( одинаковые члены обоих множеств)
a & b
a.intersection(b)
# Union. Объединение (члены обоих множеств)
a | b
a.union(b)
# Difference. Разность множества (члены только первого множества, но не второго)
a - b
a.difference(b)
# Difference. Разность множества (члены только второго множества, но не первого)
b - a
b.difference(a)
# Symmetric_difference. Исключающее ИЛИ (элементы или первого, или второго множества, но не общие. Эксклюзивные элементы)
a^b
a.symmetric_difference(b)
# Является ли множество подмножеством. Is subset?
a <= b
a.issubset(b)
# Является ли множеством множеств. Is Superset?
a >= b
a.issuperset(b)
b >= a
b.issuperset(a)