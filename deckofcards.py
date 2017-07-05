'''
'''

class Card(object):
    def __init__(self, suit, name, value, color):
        self.suit = suit
        self.name = name
        self.value = value
        self.color = color
    def __str__(self):
        return "suit: {} name: {} value: {} color: {} ".format(
            self.suit,
            self.name,
            self.value,
            self.color)

class Deck(object):
    def __init__(self):
        self.cards = []
        

deal1 = [
Card("Ace",1),
Card("Two", 2),
Card("Three", 3),
Card("Four", 4),
Card("Five", 5),
Card("Six", 6),
Card("Seven", 7),
Card("Eight", 8),
Card("Nine", 9),
Card("Ten", 10),
Card("Jack", 10),
Card("Queen", 10),
Card("King", 10)]

d = Deck()
d.addSuit(deal1, "Hearts", "red")
print d
print d.cards[0]

#print __str__(array1)
