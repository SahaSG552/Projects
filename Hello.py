a = input().split()

my_list = [[]]
for k in range(1,len(a)):
    for i in range(len(a)):
        if len(a[i:i+k]) == k:
            my_list.append(a[i:i+k])
my_list.append(a[:])
print(my_list)