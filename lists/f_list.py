
empty_list = [2, 6, 54, 9, 1, 3, 5, 23, 17]
# empty_list.sort()     #return sorted list
sorted(empty_list)    #return serted copy of list
print(sorted(empty_list, reverse=True), 'len is: %d' % len(empty_list)) #define the len of list

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
freedays = ['Saturday']
freedays.append('Sunday') # add item to end of list
weekdays.extend(freedays)   # add second list to the first
# weekdays += freedays # the same to up


big_birds = ['emu', 'ostrich', 'cassowary', 'emu']
big_birds.insert(1, 'Pinguin')  # insert in position
big_birds.insert(10, 'Last_bird')  # insert in the end
# print(str(big_birds) +'\n We delete element: "' + big_birds[3]+ '"')
# del big_birds[3]    # del is a function, not a method
print(big_birds, '\n', ' We delete element: "Pinguin" and the last element: %s' % str(big_birds[-1]))
big_birds.remove('Pinguin') # remove item for value
big_birds.pop()     # return and delete item from the end
print(big_birds)
small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']

all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]
another_empty_list = list()
a_tuple = ('ready', 'fire', 'aim')
birthday = '20/04/1987'

# print(str(weekdays) + '\n' + str(big_birds))
# print(list(a_tuple))
# print(birthday.split('/'))
# print(all_birds[1][0])

print('Friday is %d day in a week' % (weekdays.index('Friday') + 1))
print('dodo' in extinct_birds)
print(big_birds.count('emu'))   # count time of word in a list