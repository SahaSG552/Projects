with open(r'C:\Users\sahas\Downloads\1014 (1).bpp', 'r+') as bpp:
    while bpp.readline()[:7] != '[PROGRAM]':
        print(bpp.readline())