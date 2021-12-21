# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
n = 3
cr = ["3 8 1",
      "2 4 6",
      "7 0 5"
     ]
matrix = [[int(i) for i in cr[k].split()] for k in range(n)]     
matrix1 =[]
flag = 0
a = 0
b = 0
c = 0
d = 0
for i in range (n):
    c += matrix[i][i]
    d += matrix[i][n-i-1]
    for k in range (n):
        matrix1.append(matrix[i][k])
        a += matrix[i][k]
        b += matrix[k][i]
    if sum(matrix[0]) != a or sum(matrix[0]) != b:
        flag = 1
    a = 0
    b = 0
if sum(matrix[0]) != c or sum(matrix[0]) != d:
    flag = 1

matrix2 = [i for i in range (1, n*n+1)]
if sorted(matrix1) != matrix2:
    flag = 1

print("NO" if flag else "YES")