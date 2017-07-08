'''
    funfunctions.py
    Leif Anderson 7/8/17
'''

def oddeven():
    for i in range(1, 2001):
        if i % 2 == 0:
            print 'Number is ' + str(i) + '. This is an even number.'
        else:
            print 'Number is ' + str(i) + '. This is an odd number.'

oddeven()

def multiply(arrayIn, multiplier):
    arrayOut = []
    arrayLength = len(arrayIn)
    for i in range(0, arrayLength):
        arrayOut.append(arrayIn[i] * multiplier)
    return arrayOut

a = [2, 4, 10, 16]
print multiply(a, 5)

def layered_multiples(arrayIn):
    arrayOut = []
    subArray = []
    for i in range(0, len(arrayIn)):
        for j in range(0, arrayIn[i]):
            subArray.append(1)
        arrayOut.append(subArray)
        subArray = []
    return arrayOut

b = [2, 4, 5]
print layered_multiples(multiply(b,3))
