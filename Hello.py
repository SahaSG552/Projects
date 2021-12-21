a = "d6"
n = 8
c = []
[c.append(chr(97+i)) for i in range(n)]
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix = [["."]*n for _ in range(n)]
matrix[n-int(a[1])][c.index(a[0])] = "N"
x = n-int(a[1])
y = c.index(a[0])

INX = 0
for i in range(n):
    for j in range(n):
        INX = (x - j) * (y - i)
        if INX == 2 or INX == -2:
            matrix[j][i] = "*"

[print(*r) for r in matrix]