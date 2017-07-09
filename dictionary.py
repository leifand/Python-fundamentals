'''
    dictionary.py
    Leif Anderson 7/8/17
'''

dojo = {
        'Ninjas': [
            {'fname' : 'Blaze', 'lname' : 'Hayes'},
            {'fname' : 'Master', 'lname' : 'Chief'},
            {'fname' : 'Steve', 'lname' : 'Jobs'},
            {'fname' : 'Bill', 'lname' : 'Gates'}
            ],
        'Sensei': [
            {'fname' : 'The', 'lname' : 'Authman'},
            {'fname' : 'Socrates', 'lname' : 'Athens'}
            ]
        }

def printDictionary(dictionary):
    keys = dictionary.keys()
    keys.reverse()
    keyslen = len(keys)
    for i in range(0, keyslen):
        print keys[i] + ' : ' + dictionary[keys[i]]

def printDojo(nested_dict):
    keys = nested_dict.keys()
    keys.reverse()
    keyslen = len(keys)
    for i in range(0, keyslen):
        print keys[i] + ' :'
        lst = nested_dict[keys[i]]
        lstlen = len(lst)
        for j in range(0, lstlen):
            printDictionary(lst[j])

printDojo(dojo)
