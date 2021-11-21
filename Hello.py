a = int(input())
b = [[1]*i for i in range (a+1)]

for i in range(0, len(b)):
    for j in range(1,len(b[i])-1):
        b[i][j] = b[i-1][j-1] + b[i-1][j]
    if i > 0: print(*b[i])