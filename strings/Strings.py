poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

word = 'the'

print(len(poem), poem[:13], poem.startswith('All'), poem.endswith('That\'s all, folks!'))
print('First position of word "the" is: %d' % poem.find(word))
print('Last position of word "the" is: %d' % poem.rfind(word))
print('Coun of word "the" is: %d' % poem.count(word))
print('Are all characters of poem number: %s' % str(poem.isalnum()))