class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.hard, self.soft = self._points()

class NumberCard(Card):
    
    def _points(self):
        return (int(self.rank), int(self.rank))

    
class AceCard(Card):
    
    def _points(self):
        return(1, 11)

    
class FaceCard(Card):
    
    def _points(self):
        return (10, 10)


class Suit:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'),\
                              Suit('Heart','♥'), Suit('Spade','♠')

def card(rank,suit):
    if rank == 1 :
        return AceCard("A",suit)
    elif 2 <= rank < 11:
        return NumberCard(str(rank), suit)
    elif 11 <= rank <14:
        name = {11:"j", 12:"q", 13:"k"}[rank]
        return FaceCard(name, suit)
    else:
        raise Exception("range out of range")

def card2(rank,suit):
    class_ = {1:AceCard, 11:FaceCard,
              12:FaceCard, 13:FaceCard}.get(rank, NumberCard)
    return class_(rank, suit)


"""using superclass"""

class Cards:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft


class NumberCard2(Cards):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)

class AceCard2(Cards):
    def __init__(self, rank, suit):
        super().__init__("A", suit, 1, 11)

class FaceCard2(Cards):
    def __init__(self, rank, suit):
        super().__init__({11:"J", 12:"Q", 13:"K"}[rank], suit, 10, 10)


"""making function to call the currect class """
def card3(rank, suit):
    if rank == 1 : return AceCard2(rank,suit)
    elif 2 <= rank < 11: return NumberCard2(rank,suit)
    elif 11 <= rank < 14: return FaceCard2(rank,suit)
    else:
        raise Exception( " Rank out of range" )

def card33(rank, suit):
    if rank not in range(1,14):
        raise Exception( "Rank out of range" )
    class_ = {1:"AceCard2", 11:"FaceCard2", 12:"FaceCard2",
              13:"FaceCard2"}.get(rank,"NumberCard2")
    return class_(rank,suit)

"""makina a deck """
d = [ card3(r,s) for r in range(1,14) for s in [Club, Diamond, Heart, Spade]]
"""to shack the deck use random.shuffle(deck)"""
from random import shuffle
shuffle(d)
hand = [d.pop() for _ in range(13)]


"""here we did three thingd we create hand and we shake the deck and we take
a hand from deck collection,, but this is a bad design we can use a general
design strategies for this 3 steps and this is called facade pattern or
wrapper design -- incapsulation --"""

class Deck:
    def __init__(self):
        from random import shuffle
        self._cards = [card3(r,s) for r in range(1,14) for s in \
                       [Club, Diamond, Heart, Spade]]
        shuffle(self._cards)
        
    def pop(self):
        return self._cards.pop()
    def left(self):
        return len(self._cards)

""" passing  a list as parameter lets as inherted all list methods, like pop()
,append().... and so on, with this the created class going to have
all list methods"""
class Deck2(list):
    def __init__(self):
        super().__init__(card3(r,s) for r in range(1,14) for s in \
                       [Club, Diamond, Heart, Spade])
        from random import shuffle
        shuffle(self)

"""what is we need more then one deck to play a game ??
and I want to take some cards out of the game as they do in casinos"""
class Deck3(list):
    def __init__(self,decks = 1):
        super().__init__()
        for _ in range(decks):
            self.extend(card3(r,s) for r in range(1,14) for s in \
                       [Club, Diamond, Heart, Spade])
        from random import randint, shuffle
        shuffle(self)
        #to take some cards out of the game,
        burn = randint(1,52)
        for _ in range(burn): self.pop()
        
"""when we nesting for loops from normal style to generating style, in generating
style we start from deep for loop to up:
   for i in a:
       for j in b:
          for k in f:
 ==> [ for k in f for j in b for i in a] """

class Deck4(list):
    def __init__(self, decks):
        super().__init__(card3(r,s) for r in range(1,14) for s in \
                       [Club, Diamond, Heart, Spade] for _ in range(decks))
        from random import shuffle, randint
        shuffle(self)
        for _ in range(randint(1,52)): self.pop()
        
        
    
"""create class for a heand which will have methods for hard and soft points """
class Hand:
    def __init__(self, dealer_card):
        self.dealer_card = dealer_card
        self.cards = []
    def total_hard(self):
        return sum(c.hard for c in self.cards)
    def total_soft(self):
        return sum(c.soft for c in self.cards)

"""create an instance of hand """
d = Deck2()
h = Hand(d.pop())
h.cards.append(d.pop())
h.cards.append(d.pop())

"""make another hands  that will we no need to do appending after creating
a hand """

class Hand2:
    def __init__(self,leader_card,*cards):
        self.leader_card = leader_card
        self.cards = list(cards)
    def total_hard(self):
        return sum(c.hard for c in self.cards)
    def total_soft(self):
        return sum(c.soft for c in self.cards)

h2 = Hand2(d.pop(), d.pop(), d.pop())

"""build composite object in a single statement"""
class Hand22:
    def __init__(self,deck, number_cards):
        self.leader_card = deck.pop()
        self.cards = [deck.pop() for c in range(number_cards)]
    def total_hard(self):
        return sum(c.hard for c in self.cards)
    def total_soft(self):
        return sum(c.soft for c in self.cards)

"""stateless objects with out __ini__()  strategy object..
its a cl=ollection od method functions """


"""multi-strategy __init__(),, clone an object or freeze an object
when an object is froozed we can use it as a dictionaries keys,,
is like set and frozenset built-in classes"""

class Hand3:
    def __init__(self, *args, **kw):
        if len(args) == 1 and isinstance(args[0], Hand3):
            other = args[0]
            self.leader_card = other.leader_card
            self.cards = other.cards
        else:
            dealer_card, *cards = args
            self.leader_card = dealer_card
            self.cards = list(cards)

d = Deck2()
h = Hand3(d.pop(), d.pop(), d.pop())
memonto = Hand3(h)
"""with this steps we have create a hand memonto from  h, memonto is a copy of
the h hand,, in end of the game we can compare the orginal hand h with memonto
to ensure that no card was changed,, by this we made a forzen hand """



