'''
    towers.py
    Leif Anderson 6/13/18
'''

def towers(n, source, destination, intermediate):
    if n == 1: 
        print "move " + str(n) + " from " + str(source) + " to " + str(destination)
    else:
        towers(n-1, source, intermediate, destination)
        print "move " + str(n) + " from " + str(source) + " to " + str(destination)
        towers(n-1, intermediate, destination, source)

''' test'''
towers(3, "A", "C", "B")
towers(20, "A", "C", "B")