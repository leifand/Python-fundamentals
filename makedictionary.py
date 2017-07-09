'''
    makedictionary.py
    Leif Anderson 7/8/17
'''

a = ['Blaze', 'Daryl', 'Mike', 'Kevin', 'Leif']
b = ['Ferrari', 'Lamboughini', 'Cobra AC', 'Porsche']

def chkVal(values, index):
    # give a default val if vals[i] is undefined
    retVal = 'walking'
    if index < len(values):
        retVal = values[index]
    return retVal

def mergeinto(dict, keys, values):
    lenkeys = len(keys)
    for i in range(0, lenkeys):
            dict[keys[i]] = chkVal(values, i)

def makeDictionary(list1, list2):
    retDict = {}
    len1 = len(list1)
    len2 = len(list2)
    if len1 >= len2:
        mergeinto(retDict, list1, list2)
    else:
        mergeinto(retDict, list2, list1)
    return retDict

print a
print b

print makeDictionary(a, b)
print '>>>>>>>>>>>>>>>>>>'
print makeDictionary(b, a)
