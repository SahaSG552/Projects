rows, cols = 3, 4
matrix = ['0 1 -2 4'.split(),
        '1 2 5 5'.split(),
        '5 1 8 9'.split()]
matrix = [[int(i) for i in matrix[k]] for k in range(rows)]



# rows, cols = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(rows)]
maximum = -9999999999
for i in range(rows):
	if max(matrix[i]) > maximum:
		maximum = max(matrix[i])
		find_row, find_col = i, matrix[i].index(maximum)

print(find_row, find_col)