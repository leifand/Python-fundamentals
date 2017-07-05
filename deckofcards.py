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
        self.cardnames = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
        self.cards = []
        for i in range(0, 4):
            for j in range(0, 10):
                if i == 0:
                    self.cards.append(Card("Hearts", self.cardnames[j], j+1, "red"))
                elif i == 1:
                    self.cards.append(Card("Diamonds", self.cardnames[j], j+1, "red"))
                elif i == 2:
                    self.cards.append(Card("Spades", self.cardnames[j], j+1, "black"))
                elif i == 3:
                    self.cards.append(Card("Clubs", self.cardnames[j], j+1, "black"))
            for j in range(10, 13):
                if i == 0:
                    self.cards.append(Card("Hearts", self.cardnames[j], 10, "red"))
                elif i == 1:
                    self.cards.append(Card("Diamonds", self.cardnames[j], 10, "red"))
                elif i == 2:
                    self.cards.append(Card("Spades", self.cardnames[j], 10, "black"))
                elif i == 3:
                    self.cards.append(Card("Clubs", self.cardnames[j], 10, "black"))

x = Deck()
print x
for z in x.cards:
    print z
print len(x.cards)


'''
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
'''
