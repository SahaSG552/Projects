# number = input()
number = "8 78 79 6 70 7 58 5".split()
count = 0
i = 1
while i < len(number):
    if int(number[i]) > int(number[i-1]):
        count += 1
    i += 1
print(count)