name = 'роскомнадзор'
letters = [_ for _ in set(name)]
letters.sort()
for i in letters:
    print('')
print(letters)