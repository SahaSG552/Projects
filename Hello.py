def read_csv():
    with open("data.csv", "r", encoding="utf-8") as f:
        keys, values = f.readline().strip().split(","), [
            i.strip().split(",") for i in f.readlines()
        ]
        d = [dict(zip(keys, v)) for v in values]
    return d


print(read_csv())
