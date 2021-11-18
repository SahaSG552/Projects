name = 'госдеп'
word = name + ' запретил букву'
letters = [_ for _ in set(word) if _.isalpha()]
letters.sort()
for i in letters:
    print(word, i)
    word = word.replace(i, '').strip(' ').replace('  ', ' ')
print('Hello, GitHub!')