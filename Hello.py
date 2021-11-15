# number = input()
number = "216 39 87 0 0 1 1".split()
for i in range (1, len(number), 2):
    number[i], number[i-1] = number[i-1], number[i]
print(*number)