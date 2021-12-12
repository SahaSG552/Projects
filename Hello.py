rows, cols = 3, 4
matrix = ['11 12 13 14'.split(),
        '21 22 23 24'.split(),
        '31 32 33 34'.split()]
matrix = [[int(i) for i in matrix[k]] for k in range(rows)]
swap_cols = "0 1"
swap_cols = [int(i) for i in swap_cols.split()]

# rows, cols = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(rows)]
# swap_cols = [int(i) for i in input().split()]


for k in range(rows):
	matrix[k][swap_cols[0]], matrix[k][swap_cols[1]] = matrix[k][swap_cols[1]], matrix[k][swap_cols[0]]
	print(*matrix[k], sep=' ')