#bpp_path = r"E:\Работа\РАБОЧИЕ ПРОЕКТЫ\CNC\Ошибки\2004.bpp"
import tkinter as tk
# from tkinter import filedialog   # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

root = tk.Tk()
root.withdraw()
# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
bpp_path = askopenfilename(
    initialdir="/Работа/РАБОЧИЕ ПРОЕКТЫ/CNC/Ошибки", title="Select a file", filetypes=[("BPP", "*.bpp")]
)

panel_side = {'0':'0','1':'4','2':'1','3':'2','4':'3','5':'5'}
panel_side2 = ['1', '2', '3', '4']
bw_version = 0

with open(bpp_path, 'r') as bpp, open(bpp_path[:-4] + '-2' + ".bpp", 'w') as new_bpp:
    line = bpp.readline()
    # define x & y values
    while 'PAN=LPY' not in line:
        line = bpp.readline()
        if 'PAN=LPX' in line: 
            x = float(line.split('|')[1])
        if 'PAN=LPY' in line: 
            y = float(line.split('|')[1])
    bpp.seek(0)
    print()
    # write changes to new file
    while line:
        line = bpp.readline()
        # switch x & y
        if line.rstrip() == 'VER=150':
            bw_version = 1
            line = 'VER=120\n'
        if 'PAN=LPX' in line: 
            x_to_y = line.split('|')
            line = ('|').join([x_to_y[0], str(y), ('|').join(x_to_y[2:])])
        if 'PAN=LPY' in line: 
            x_to_y = line.split('|')
            line = ('|').join([x_to_y[0], str(x), ('|').join(x_to_y[2:])])
        if bw_version == 1:
            if '"BV"' in line:
                new_line = line.split(',')
                line = (',').join([(',').join(new_line[:5]), new_line[5][:-1] + panel_side[new_line[5][-1]],
                ' "' + panel_side[new_line[6][-2]] + '"', new_line[8], new_line[7], (',').join(new_line[9:28]),
                " 0" if new_line[28] == " 90" else " 90", (',').join(new_line[29:])])
            if '"BH"' in line:
                new_line = line.split(',')
                line = (',').join([(',').join(new_line[:5]), new_line[5][:-1] + panel_side2[new_line[5][-1]],
                (',').join(new_line[6:])])
        else:
            if 'BV,' in line:
                new_line = line.split(',')
                print()
                line = (',').join([(',').join(new_line[:3]), new_line[3][:-1] + panel_side[new_line[3][-1]],
                ' "' + panel_side[new_line[4][-2]] + '"', new_line[6], new_line[5], (',').join(new_line[7:26]),
                '0' if int(new_line[26].split('.')[0]) == 90 else '90', (',').join(new_line[27:])])
            if 'BH,' in line:
                new_line = line.split(',')
                line = (',').join([(',').join(new_line[:3]), new_line[3][:-1] + panel_side[new_line[3][-1]],
                (',').join(new_line[4:])])
        new_bpp.write(line)
