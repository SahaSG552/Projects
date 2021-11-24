def print_matrix(matrix, n, width):
    for r in range(n):
        for c in range(n):
            print(str(matrix[r][c]).ljust(width), end=' ')
        print()

matrix  = [[277, -93, 11, 0],
           [9, 43, 6, 87],
           [4567, 8, 290, 7]]
n = len(matrix)
width = max([max(j) for j in [[len(str(k)) for k in matrix[i]] for i in range(len(matrix))]]) + 1

# s = 0
# for li in matrix:
#     for i in range(len(li)):
#         if len(str(li[i])) > s:
#             s = len(str(li[i]))

# print_matrix(matrix,n,width)

cols = 2
rows = 4
cols, rows = int(input()), int(input())
a = [[input() for _ in range(rows)] for _ in range(cols)]
for i in range(len(a)):
    print(*a[i], end='\n')