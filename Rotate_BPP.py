bpp_path = r'E:\Работа\РАБОЧИЕ ПРОЕКТЫ\CNC\Ошибки\Test.bpp'
panel_side = {' 0 : 0': ' 0 : 0',' 0 : 1': ' 0 : 4',' 0 : 2': ' 0 : 1',' 0 : 3': ' 0 : 2',' 0 : 4': ' 0 : 3'}

with open(bpp_path, 'r') as bpp, open(bpp_path.rstrip(bpp_path.split("\\")[-1]) + "Test2.bpp", 'w') as new_bpp:
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
        if 'PAN=LPX' in line: 
            x_to_y = line.split('|')
            line = ('|').join([x_to_y[0], str(y), ('|').join(x_to_y[2:])])
        if 'PAN=LPY' in line: 
            x_to_y = line.split('|')
            line = ('|').join([x_to_y[0], str(x), ('|').join(x_to_y[2:])])
        if '"BV"' in line:
            new_line = line.split(',')
            line = (',').join([(',').join(new_line[:5]), panel_side[new_line[5]],
            new_line[6], new_line[8], new_line[7], (',').join(new_line[9:28]),
            " 0" if new_line[28] == " 90" else " 90", (',').join(new_line[29:])])
        if '"BH"' in line:
            new_line = line.split(',')
            line = (',').join([(',').join(new_line[:5]), panel_side[new_line[5]],
            (',').join(new_line[6:])])
        new_bpp.write(line)
