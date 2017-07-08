'''
    stars.py
    Leif Anderson 7/8/17
'''

def stars1(listIn):
    listLength = len(listIn)
    for i in range(0, listLength):
        star_string = ''
        for j in range(0, listIn[i]):
            star_string += '*'
        print star_string

a = [4, 6, 1, 3, 5, 7, 25]
stars1(a)

def stars2(listIn):
    listLength = len(listIn)
    for i in range(0, listLength):
        print_char = ''
        if isinstance(listIn[i], str):
            print_char = listIn[i][0].lower()
            innerLength = len(listIn[i])
        else:
            print_char = '*'
            innerLength = listIn[i]
        print_string = ''
        for j in range(0, innerLength):
            print_string += print_char
        print print_string

b = [4, 'Tom', 1, 'Michael', 5, 7, 'Jimmy Smith']
stars2(b)
