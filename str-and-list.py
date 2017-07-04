'''
    str-and-list.py
    Leif Anderson 7/3/17
'''

# Find and Replace example
def exFindReplace():
    words = "It's thanksgiving day. It's my birthday too!"
    print words.find("day")
    words = words.replace('day', 'month', 1)
    print words

exFindReplace()

# a function to return the min and max values of any given array
def MinMax(listIn):
    print min(listIn)
    print max(listIn)

myList = [2, 54, -6, 70, 43, 101, -7]
MinMax(myList)

# a function to return the first and last elements of a list
def FirstLast(listIn):
    print listIn[0]
    print listIn[len(listIn) - 1]
    retList = [listIn[0],listIn[len(listIn) - 1]]
    return retList

yourList = ["Bacon", 33, -100, 98, "Cheddar"]
print FirstLast(yourList)

# complicated list manipulation function: see exercise notes!
def NewList(listIn):
    listOut = []
    listTemp = []
    list.sort(listIn)
    splitPoint = len(listIn)/2
    print splitPoint
    for i in range(0, splitPoint):
        listTemp.append(listIn[i])
    listOut.append(listTemp)
    for j in range(splitPoint, len(listIn)):
        listOut.append(listIn[j])
    return listOut

anotherList = [19, 2, 56, -200, 1, 98, 34, 10, -2, 6]
print NewList(anotherList)
