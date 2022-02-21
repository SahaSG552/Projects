a = 5
summa = a
# digits = len(str(a))
for i in range(len(str(a))):
    summa1 = summa
    for digit in str(summa1):
        summa += int(digit)
    print(summa)
print(summa1)
