import tkinter as tk

# from tkinter import filedialog   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames

root = tk.Tk()
root.withdraw()

bxf_paths = askopenfilenames(
    parent=root,
    initialdir="/Работа/РАБОЧИЕ ПРОЕКТЫ/bazis_impor/ORD/",
    title="Choose a file",
    filetypes=[("BXF2", "*.bxf2")],
)


new_bxf_path = (
    ("/").join((bxf_paths[0].split("/"))[:-1])
    + "/merged_"
    + bxf_paths[0].split("/")[-2]
    + ".bxf2"
)

x, y, z = 0, 0, 0
move_x = []  # move every next detail to x
for i, bxf_path in enumerate(bxf_paths):
    machining = []
    partlinks = []
    with open(bxf_path, "r") as bxf, open(new_bxf_path, "w") as new_bxf:
        try:
            for line in bxf:
                if "<machining " in line:
                    machining.append(line.rstrip("\n"))
                if "<partLink " in line:
                    partlinks.append(line.rstrip("\n"))
                    partlinks.append(
                        f'<transformations>\n<transformation translation="{sum(move_x)} 0 0"/>\n</transformations>\n</partLink>'
                    )
                if "<extent>" in line:
                    x, y, z = list(
                        map(
                            float,
                            (
                                (line.lstrip("<extent>")).rstrip("</extent>\n")
                            ).split(" "),
                        )
                    )
                    move_x.append((x + 150) * (i > 0))
                    move_x[i] = sum(move_x)

            next(bxf)
        except StopIteration:

            print(move_x[i])
            print(x, y, z)
            print(move_x)
            machining = list(set(machining))
            print(*machining, sep="\n")
            print()
            print(*partlinks)
            print()
