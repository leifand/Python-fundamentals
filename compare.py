'''
    compare.py
    Leif Anderson 7/5/17
'''

def compareArrays(arr1, arr2):
    identical = True
    if len(arr1) != len(arr2):
        identical = False
    else:
        for i in range(0, len(arr1)):
            if arr1[i] != arr2[i]:
                identical = False
    if identical:
        print 'The lists are the same!'
    else:
        print 'The lists are not the same!'

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]
list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]
list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

compareArrays(list_one, list_two)
compareArrays(list_three, list_four)
compareArrays(list_five, list_six)
compareArrays(list_seven, list_eight)
