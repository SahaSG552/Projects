with open("lines.txt", "r", encoding="utf-8") as f:
    a = [i.strip() for i in f.readlines()]
    b = list(filter(lambda x: len(x.strip()) == max(map(len, a)), a))
    print(*b, sep="\n")
