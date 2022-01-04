def print_matrix(rows, cols, matr):
    for i in range (rows):
        for j in range (cols):
            print(str(matr[i][j]).ljust(len(str(666))), end=' ')
        print()
        
# r = int(input())
# c = r
# matrix1 = [[int(i) for i in input().split()] for _ in range(r1)]
# m = int(input())
import copy
r = 3
c = r
m = 5
matrix1 = [
           [1, 2, 1], 
           [3, 3, 3],
           [1, 2, 1],
          ]
# matrix2 = copy.deepcopy(matrix1)
matrix2 = list(matrix1)

matrix = [[0 for _ in range(c)] for _ in range(r)]

for l in range (m-1):
    for i in range (r):
        for j in range (r):
            for k in range (r):
                matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    matrix2 = matrix
    matrix = [[0 for _ in range(c)] for _ in range(r)]            

print_matrix(r, c, matrix2)