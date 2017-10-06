years_list = [1987, 1988, 1989, 1990, 1991, 1992]
for i in years_list:
    if (i - years_list[0] == 3):
        print('In a year %d i was 3 years' % i)

for j in years_list:
    if (years_list.index(j) == 0):
        pr_year = 0
        continue
    if (j - years_list[0] > pr_year):
        pr_year = j - years_list[0]
    else: continue
print('In a year %d i was %d years' % (years_list[0] + pr_year, pr_year))

things = ['mozzarella', 'cinderella', 'salmonella']
things[1].capitalize()
del things[2]
print(things)

surpeise = ['Groucho', 'Chico', 'Harpo']
surpeise[2].lower()
surpeise.reverse()
surpeise[2].capitalize()
print(surpeise[2].lower())

e2f = {
    'dog':'chien',
    'cat':'chat',
    'walrus':'morse'
}
print(e2f['walrus'])