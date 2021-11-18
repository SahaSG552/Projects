n = int(input())
refrigerators = []
b = [c for c in 'anton']
for virus in range(n):
    #отсеиваем лишние символы
    a = [i for i in input() if i.isalpha() and i in b]
    i = 0
    k = 0
    count = 0
    while i < len(a):
        if count == 5: 
            count = 0
            refrigerators.append(virus)
            break
        if a[i] == b[k]:
            k +=1
            count += 1
            continue
        else:
            i += 1
print(*refrigerators)