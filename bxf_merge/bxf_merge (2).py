import tkinter as tk
import os

# from tkinter import filedialog   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilenames

try:
    root = tk.Tk()
    root.withdraw()
    bxf_paths = askopenfilenames(
        parent=root,
        initialdir="",
        title="Choose bxf2 files",
        filetypes=[("BXF2", "*.bxf2")],
    )

    order_name = bxf_paths[0].split("/")[-2]
    order_path = ("/").join((bxf_paths[0].split("/"))[:-1])
    new_bxf_path = (
        order_path
        + "/-"
        + order_name
        + " ("
        + str(len(bxf_paths))
        + ")"
        + ".bxf2"
    )

    # combine info from files
    machinings = []
    partlinks = []
    parts = []

    x, y, z = 0, 0, 0  # detail coordinates
    move_x = [0]  # move every detail next to previous + 150 along x axis
    move_xx = [0]
    for i, bxf_path in enumerate(bxf_paths):
        machining = []
        partlink = []
        part = []
        with open(
            bxf_path, "r"
        ) as bxf:  # , open(new_bxf_path, "w") as new_bxf
            counter = 0  # counting down lines in file
            part_counter = 1000000000  # var to check where to start record part information
            line = bxf.readline()
            while "</part>" not in line:
                line = bxf.readline()
                if "<machining " in line:
                    machining.append(line.rstrip("\n"))
                if "<partLink " in line:
                    partlink.append(line.rstrip("\n"))
                    [
                        partlink.append(j)
                        for j in [
                            "<transformations>",
                            "",
                            "</transformations>",
                            "</partLink>",
                        ]
                    ]
                if "<extent>" in line:
                    x, y, z = list(
                        map(
                            float,
                            (
                                (line.lstrip("<extent>")).rstrip("</extent>\n")
                            ).split(" "),
                        )
                    )
                    move_x.append(x + 150)
                    move_xx.append(sum(move_x))
                if "<part " in line:
                    part_counter = counter
                if part_counter <= counter:
                    part.append(line.rstrip("\n"))
                counter += 1

        partlink[2] = f'<transformation translation="{move_xx[i]} 0 0"/>'
        machining = list(set(machining))
        machinings.extend(machining)
        machinings = list(set(machinings))
        partlinks.extend(partlink)
        parts.extend(part)
        # print(*machinings, sep="\n")
        # print()
        # print(*partlinks, sep="\n")
        # print()
        # print(*parts, sep="\n")
        # print()

    with open("Header.txt", "r") as header, open(new_bxf_path, "w") as new_bxf:
        line = header.readline()
        while line:
            line = header.readline()
            if "MACHININGS" in line:
                line = "\n".join(machinings)
            if "PARTLINKS" in line:
                line = "\n".join(partlinks)
            if "PARTS" in line:
                line = "\n".join(parts)
            new_bxf.write(line)
        os.startfile(order_path)  # open destination folder

except IndexError:
    pass
