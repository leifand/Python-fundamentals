'''
    typelist.py
    Leif Anderson 7/3/17
'''

def processList(lst):
    strings = ''
    sum = 0
    stringFlag = False
    numFlag = False
    for i in range(0, len(lst)):
        if isinstance(lst[i], int) or isinstance(lst[i], float):
            sum = sum + lst[i]
            numFlag = True
        elif isinstance(lst[i], str):
            strings = strings + lst[i] + ' '
            stringFlag = True
        else: pass
    if stringFlag and numFlag:
        print "The array you entered is of mixed type."
        print "String: " + strings
        print "Sum: " + str(sum)
    elif stringFlag:
        print "The array you entered is of string type."
        print "String: " + strings
    elif numFlag:
        print "The array you entered is of numeric type."
        print "Sum: " + str(sum)
    else: pass

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

processList(l1)
processList(l2)
processList(l3)
