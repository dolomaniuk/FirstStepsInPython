empty_dict = {}
briece = {
    "day" : "A period of twenty-four hours, mostly misspent",
    "positive" : "Mistaken at the pot of one's voise",
    "misfortune" : "The kind of fortune that never misses"
    }
lol = [['a','b'], ['c','d'],['e','f']]
dict(lol)
lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
dict(lot)
tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
dict(tol)
los = [ 'ab', 'cd', 'ef' ]
dict(los)
tos = ('ab', 'cd', 'ef')
dict(tos)

pythons = {
    'Chapman':'Graham',
    'Cleese':'John',
    'Idle':'Eric',
    'Jones':'Terry',
    'Palin':'Michael',
}

pythons['Gilliam'] = 'Terry' # add new item to dict

others = {
    'Marx':'Grucho',
    'Howard':'Moe'
}

pythons.update(others)
print(pythons)
del pythons['Howard']

# pythons.clear()
key = 'Marx1'
print(pythons.get(key, "%s isn't in pythons" % key)) # find key in a dict