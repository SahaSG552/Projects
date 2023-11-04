my_dict = {}
structure = []
with open("LITE_ISIGHT_EXPORT.xml", "r") as f:
    data = f.read()
    for line in data.split("\n"):
        if line.lstrip().startswith("<Var "):
            var_id = float(line.split()[2].split('"')[1])
            my_dict[var_id] = line
        elif line:
            structure.append(line)

print(structure)
sorted_by_id = [v for _, v in sorted(my_dict.items(), key=lambda x: x[0])]

with open("LITE_ISIGHT_EXPORT_sorted.xml", "w") as f:
    [f.write(structure[i]+"\n") for i in range(2)]
    [f.write(line+"\n") for line in sorted_by_id]
    f.write(structure[2])
