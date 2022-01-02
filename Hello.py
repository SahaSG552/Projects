# r, c = map(int, input().split())
r, c = 6, 7
matrix = [[0 for _ in range(c)] for _ in range(r)]

def print_matrix(rows, cols):
    for i in range (rows):
        for j in range (cols):
            print(str(matrix[i][j]).ljust(len(str(rows*cols))), end=' ')
        print()

n = 1
low_c = 0
high_c = c - 1
low_r = 0
high_r = r - 1

for i in range(int(c // 2 + 1)):
    
    for j in range(low_c, high_c + 1):
        if n > r * c: break
        matrix[low_c][j] = n
        n += 1
    for j in range(low_r + 1, high_r + 1):
        if n > r * c: break
        matrix[j][high_c] = n
        n += 1
    for j in range(high_c - 1, low_c - 1, -1):
        if n > r * c: break
        matrix[high_r][j] = n
        n += 1
    for j in range(high_r - 1, low_r, -1):
        if n > r * c: break
        matrix[j][low_r] = n
        n += 1
     

    low_c += 1
    high_c -= 1
    low_r += 1
    high_r -= 1
print_matrix(r, c)