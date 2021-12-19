# cr = int(input())
a = 4
cr = ["5 3 7 1",
"3 5 4 5",
"7 4 4 8",
"1 5 8 5"]
matrix = [[int(i) for i in cr[k].split()] for k in range(len(cr))]
print (*matrix,sep="\n")



# a = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(a)]

flag = 1
for i in range (a):
    for k in range(i):
        if matrix[i][k] != matrix[k][i]:
            flag = 0
            break
print("YES" if flag else "NO")