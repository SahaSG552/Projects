my_dict = {}

with open("LITE_ISIGHT_EXPORT.xml", "r") as f:
    data = f.read()
    for line in data.split("\n"):
        if line.lstrip().startswith("<Var "):
            var_id = float(line.split()[2].split('"')[1])
            my_dict[var_id] = line

[print(v) for _, v in sorted(my_dict.items(), key=lambda x: x[0])]
