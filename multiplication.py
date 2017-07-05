'''
    multiplication.py
    Leif Anderson 7/5/17
'''

def multiplicationTable():
    print 'x   1   2   3   4   5   6   7   8   9  10  11  12'
    rowString = ''
    for row in range(1, 13):
        rowString = rowString + str(row) + '   '
        for col in range(1,13):
            rowString = rowString + str(row*col) + '  '
        rowString = rowString + '\n'
        print rowString
        rowString = ''

multiplicationTable()
