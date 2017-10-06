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

for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or 'cream' in contents):
        print(name)
