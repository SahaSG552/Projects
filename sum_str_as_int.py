def sum_str_as_int(a, b):
    a, b = sorted((a, b),key=len, reverse=True)
    shortest = min(map(len, (a, b)))
    longest = max(map(len, (a, b)))
    c = "0" * (longest - shortest)
    b = c + b
    a, b = a[::-1], b[::-1]
    temp = 0
    result = ""
    for i in range(longest):
        sum_digits = temp + int(a[i]) + int(b[i])
        temp = sum_digits >= 10
        result += str(sum_digits)[-1]

    return (str(int(temp)) + result[::-1]).lstrip("0")


a = "99"
b = "9"
print(sum_str_as_int(a, b))
