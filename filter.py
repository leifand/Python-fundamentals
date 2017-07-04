'''
    filter.py
    Leif Anderson 7/3/17
'''

def processType(obj):
    if isinstance(obj, int):
        # obj is a value
        if obj >= 100:
            print "That's a big number!"
        else: print "That's a small number!"
    elif isinstance(obj, str):
        # obj is a sequence
        if len(obj) >= 50:
            print "That's a big string!"
        else: print "That's a small string!"
    elif isinstance(obj, list):
        # obj is a sequence
        if len(obj) >= 10:
            print "That's a big list!"
        else: print "That's a small list!"
        # obj is unknown
    else: print "Unknown type!"

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

processType(sI)
processType(mI)
processType(bI)
processType(eI)
processType(spI)
processType(sS)
processType(mS)
processType(bS)
processType(eS)
processType(aL)
processType(mL)
processType(lL)
processType(sI)
processType(eL)
processType(spL)
