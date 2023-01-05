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
print(bxf_paths)


new_bxf_path = (
    ("/").join((bxf_paths[0].split("/"))[:-1])
    + "/merged_"
    + bxf_paths[0].split("/")[-2]
    + ".bxf2"
)


for i, bxf_path in enumerate(bxf_paths):
    machining = []

    with open(bxf_path, "r") as bxf, open(new_bxf_path, "w") as new_bxf:
        line = bxf.readline()
        # define x & y values
        while line:
            line = bxf.readline()
            if "<machining " in line:
                machining.append(line.rstrip("\n"))
            if "<extent>" in line:
                x, y, z = list(
                    map(
                        float,
                        (
                            (line.lstrip("<extent>")).rstrip("</extent>\n")
                        ).split(" "),
                    )
                )
        machining = list(set(machining))
        print(machining)
        print(x, y, z)
