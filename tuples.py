'''
    tuples.py
    Leif Anderson 7/8/17
'''

my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def dict2tuples(dictionary): # thank you google!
    return dictionary.items()

print dict2tuples(my_dict)
