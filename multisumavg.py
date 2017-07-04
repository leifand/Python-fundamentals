'''
    multisumavg.py
    Leif Anderson 7/3/17
'''

# print odd numbers from 0 to 1000
def printOdds():
    for i in range(0,1001):
        if i % 2 != 0:
            print i;

printOdds()

# print all multiples of 5 up to 1,000,000
def printMultiples():
    multiplier = 1
    multipleOf5 = 1
    while (multipleOf5 < 1000000):
        multipleOf5 = 5 * multiplier
        multiplier = multiplier + 1
        print multipleOf5

printMultiples()

# sum all of the numbers in a list
def sumValues(listIn):
    sum = 0;
    for i in range(0, len(listIn)):
        sum = sum + listIn[i]
    return sum

aList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print sumValues(aList)

# return the average of values in a list
def avgValues(listIn):
    return sumValues(listIn) / len(listIn)

print avgValues(aList)
