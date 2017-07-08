'''
    cointoss.py
    Leif Anderson 7/8/17
'''
import random

def cointoss(n):
    toss = ''
    if n == 1:
        toss = 'head'
    else:
        toss = 'tail'
    return toss

def cointosses():
    print 'Starting the program ...'
    heads = 0
    tails = 0
    for i in range(1, 5001):
        toss = round(random.random())
        if toss == 1:
            heads += 1
        elif toss == 0:
            tails += 1
        print 'Attempt #' + str(i) + ': Tossing a coin ... Its a ' + cointoss(toss) + '! ...    Got ' + str(heads) + ' head(s) so far and ' + str(tails) + ' tail(s) so far'
    print 'Ending the program, thank you!'

cointosses()
