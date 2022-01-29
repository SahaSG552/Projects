a = ['Вижу зверей', 'Живу резвей']
#a = [sorted([i.lower() for i in a if i.isalnum()]) for _ in range(2)]
#print("YES" if a[0] == a[1] else "NO")


def dicts(sentence):
    my_dict = {}
    for i in sentence.lower():
        if i.isalpha():
            my_dict[i] = my_dict.get(i, 0) + 1
    return(my_dict)
print(("NO", "YES")[dicts('Вижу зверей') == dicts('Живу резвей')])
