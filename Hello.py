identificators = "a a a a a a a aa a a a a a aa a a! b b2 b4 b3 a4 a9 a1 a a!".split()

result = {}
for word in identificators:
    result[word] = result.get(word, -1) + 1
    if result[word] == 0:
        print(word, end=" ")
    else:
        print(word + "_" + str(result[word]), end=" ")
print()

for i in identificators:
    count = 0
    for j in range(len(identificators)):
        if identificators[j] == i:
            identificators[j] += "_" + str(count)
            count +=1
            identificators[j] = identificators[j].replace("_0","")
print(*identificators)
