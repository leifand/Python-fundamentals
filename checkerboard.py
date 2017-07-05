'''
    checkerboard.py
    Leif Anderson 7/5/17
'''

def checkerboard():
    for i in range(0, 8):
        printStar = False
        outString = ''
        if i % 2 == 0:
            printStar = True
        for j in range(0, 8):
            if printStar:
                outString += '*'
                printStar = False
            else:
                outString += ' '
                printStar = True
        print outString

checkerboard()
