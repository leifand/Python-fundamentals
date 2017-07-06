'''
    foobar.py
    Leif Anderson 7/5/17
'''

def isPerfectSquare(n):
    isPerfect = False
    for i in range(0, n):
        if i * i == n:
            isPerfect = True
            break
    return isPerfect

def isPrimeNumber(num):
    isPrime = True
    maxRange = num/2
    for i in range(2, maxRange):
        if num % i == 0:
            isPrime = False
            break
    return isPrime

def foobar():
    for i in range(99950, 100001):
        if isPerfectSquare(i):
            print "Bar"
            print i
        elif isPrimeNumber(i):
            print "Foo"
            print i
        else:
            print "FooBar"
            print i

foobar()
'''
print isPerfectSquare(24)
print isPerfectSquare(25)

print isPrimeNumber(7)
print isPrimeNumber(17)
print isPrimeNumber(77)
'''
