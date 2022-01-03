def print_matrix(rows, cols, matr):
    for i in range (rows):
        for j in range (cols):
            print(str(matr[i][j]).ljust(len(str(666))), end=' ')
        print()
        
# r1, c1 = map(int, input().split())
# matrix1 = [[int(i) for i in input().split()] for _ in range(r1)]
# input()
# r2, c2 = map(int, input().split())
# matrix2 = [[int(i) for i in input().split()] for _ in range(r2)]
# matrix = [[0 for _ in range(c2)] for _ in range(r1)]

r1, c1 = 4, 3
r2, c2 = 3, 4
matrix1 = [[6, 2, 5], 
           [4, 3, 5],
           [1, 2, 8],
           [4, 3, 9],
           ]
matrix2 = [[1, 2, 8, 4], 
           [6, 1, 5, 2],
           [4, 4, 5, 7],
           ]
matrix = [[0 for _ in range(c2)] for _ in range(r1)]

for i in range (r1):
    for j in range (c2):
        for k in range (c1):
            matrix[i][j] += matrix1[i][k] * matrix2[k][j]

print_matrix(r1, c2, matrix)