'''
    findcharacter.py
    Leif Anderson 7/5/17
'''


def containsCharacter(char, stringArray):
# returns a list of strings containing the passed in character
    arrayOut = []
    for i in range(0, len(stringArray)):
        contains = False
        for j in range(0, len(stringArray[i])):
            if char == stringArray[i][j]:
                contains = True
        if contains:
            arrayOut.append(stringArray[i])
    return arrayOut


word_list = ['hello','world','my','name','is','Anna']
char = 'o'

print containsCharacter(char, word_list)
