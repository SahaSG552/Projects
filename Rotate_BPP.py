bpp_path = r'E:\Работа\РАБОЧИЕ ПРОЕКТЫ\CNC\Ошибки\00285353 — копия.bpp'

with open(bpp_path, 'r') as bpp, open(bpp_path.rstrip(bpp_path.split("\\")[-1]) + "Test.bpp", 'w') as new_bpp:
    line = bpp.readline()
    # define x & y values
    while 'PAN=LPY' not in line:
        line = bpp.readline()
        if 'PAN=LPX' in line: 
            x = float(line.split('|')[1])
            print(line.rstrip())
        if 'PAN=LPY' in line: 
            y = float(line.split('|')[1])
            print(line.rstrip())
    bpp.seek(0)
    print()
    # write changes to new file
    while line:
        line = bpp.readline()
        # switch x & y
        if 'PAN=LPX' in line: 
            x_to_y = line.split('|')
            line = ('|').join([x_to_y[0], str(y), ('|').join(x_to_y[2:])])
            print(line.rstrip())
        if 'PAN=LPY' in line: 
            x_to_y = line.split('|')
            line = ('|').join([x_to_y[0], str(x), ('|').join(x_to_y[2:])])
            print(line.rstrip())
        new_bpp.write(line)
    bpp.seek(0)
    

    # print()
    # while line != '[VBSCRIPT]\n':
    #     line = bpp.readline()
    #     if line != '\n': print(line.rstrip().split(','))
with open(r'E:\Работа\РАБОЧИЕ ПРОЕКТЫ\CNC\Ошибки\Test.bpp', 'r+') as bpp:
    while 'PAN=LPY' not in line:
        line = bpp.readline()
        print(line.rstrip())