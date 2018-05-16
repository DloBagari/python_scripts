

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_int= int({'A':'1','J':'11','Q':'12','K':'13'}.get(self.rank, self.rank))
        self.hard, self.soft = self._points()

    """ use of repr method: this method is linked to print and repr() and format()
        the fields most be in repr() by withing (!r) """
    def __repr__(self):
        return "{__class__.__name__}(Suit = {suit.symbol!r}, Rank = {rank!r})".\
               format(__class__ = self.__class__,**self.__dict__)
    """if the class has not overrride the __str__() and it has override __repr__()
        when we call str() on the object it will use the __repr__() method """

    def __str__(self):
        return "({suit.symbol}, {rank})".format(**self.__dict__)

    def __format__(self, format_spec):
        if format_spec == "":
            return str(self)
        rs = format_spec.replace("%r", str(self.rank)).replace("%s",self.suit.symbol)
        rs = rs.replace("%%", "%")
        return rs

    def __eq__(self, other):
        try:
            return self.suit.symbol == other.suit.symbol and self.rank == other.rank
            #and self.hard == other.hard and self.soft == other.soft
        except AttrubiteError:
            return NotImplemented
    
    #__hash__ = None  # if for mutable object 
    def __hash__(self):
        return hash(self.suit.symbol) ^ hash(self.rank)

    def __bytes__(self):
        class_code = self.__class__.__name__[0]
        str_rank = {"A":"1","J":"11","Q":"12","K":"13"}.get(self.rank, self.rank)
        string = "("+" ".join([class_code, str_rank, self.suit.name])+")"
        return bytes(string, encoding='utf8')

    def __lt__(self, other):
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank_int < other.rank_int

    def __le__(self, other):
        try:
            return self.rank_int <= other.rank_int
        except AttributeError:
            return NotImplemented
    def __ne__(self, other):
        "in this method NotImplemented return True or False"
        try:
            return self.suit.symbol != other.suit.symbol and self.rank_int != other.rank_int
        except AttributeError:
            return NotImplemented
        
    def __gt__(self, other):
        try:
            return self.rank_int > other.rank_int
        except AttributeError:
            return NotImpemented
        
    def __ge__(self, other):
        try:
            return self.rank_int <= other.rank_int
        except AttributeError:
            return NotImplemented

    def __eq__(self, other):
        """in this method NotImplemented is returns a False"""
        if not isinstance(other, Card):
            return NotImplemented
        return self.rank_int == other.rank_int and self.suit.symbol == other.suit.symbol
        
    
    

    

"""any card is instance of the card class and the subclass
we can use isinstance(1,int) for find if the number is integer"""
class NumberCard(Card):
    def _points(self):
        return int(self.rank), int(self.rank)


class AceCard(Card):
    def _points(self):
        return 10, 1


class FaceCard(Card):
    def _points(self):
        return 10, 10


class Suit:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'),\
                              Suit('Heart','♥'), Suit('Spade','♠')


def card(rank, suit):
    if type(rank) == int:
        if not (1 <= rank <14):
            raise Exception("rank is out og the range ")
            
    class_ = {1: AceCard, 11: FaceCard,
              12: FaceCard, 13: FaceCard}.get(rank, NumberCard)
    return class_({1:"A",11:"J",12:"Q",13:"K"}.get(rank,str(rank)), suit)


class Deck(list):
    
    def __init__(self, size=1):
        super().__init__(card(rank, suit) for rank in range(1, 14) \
                       for suit in [Club, Diamond, Heart, Spade] \
                       for _ in range(size))
        from random import randint, shuffle
        shuffle(self)

        burn = randint(4 * size,7 * size) #set of cards to be removed
        for _ in range(burn):self.pop()


class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def hard(self):
        return sum(c.hard for c in self.cards)

    def soft(self):
        return sum(c.soft for c in self.cards)
    
    def __repr__(self):
        return "{__class__.__name__:*^{n}s}\nDealer = {dealer_card!r}\nCards:\n{_cards_str}".format\
               (__class__ = self.__class__, n=len(repr(self.dealer_card))+9, _cards_str = ",\n".join\
                (map(repr,self.cards)), **self.__dict__)

    def __str__(self):
        return ", ".join(map(repr, self.cards))

    def __format__(self,spec):
        if spec == "":
            return str(self)
        return ", ".join("{0:{fs}}".format(c, fs = spec) for c in self.cards)
    
    """special methods are the feature of python to let an object to communicate with
     another python codes
      the __str__() and repr__() methods are usually linked to repr() ,str(), print()
      format() functions, the __str__() is representation of the object for human readablity
      and __repr__() the more information about the object it like how to rebuild the
      object is full representation ofthe object"""

    def __eq__(self, other):
        #comparsion with mix classes
        if isinstance(other, int):
            return self.total_blackjack() == other
        return self.cards == other.cards and self.dealer_card == other.dealer_card

    def __lt__(self, other):
        #comparsion with mix classes
        if isinstance(other, int):
            return self.total_blackjack() < other
        try:
            return self.total_blackjack() < other.total_blackjack()
        except AttributeError:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, int):
            return self.total_blackjack() > other
        try:
            return self.total_blackjack() > other.total_blackjack()
        except AttributeError:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, int):
            return self.total_blackjack() >= other
        try:
            return self.total_blackjack() >= other.total_blackjack()
        except AttributeError:
            return NotImplemented
        
    def __le__(self, other):
        if isinstance(other, int):
            return self.total_blackjack() <= other
        try:
            return self.total_blackjack() <= other.total_blackjack()
        except AttributeError:
            return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, int):
            return self.total_blackjack() != other
        try:
            return self.total_blackjack() != other.total_blackjack()
        except AttributeError:
            return NotImplemented
    
        
        
    __hash__ = None

    def total_blackjack(self):
        hard = max(c.hard - c.soft for c in self.cards)
        soft = sum( c.soft for c in self.cards)
        if hard + soft <= 21:
            return hard + soft
        return soft
        
    

""" the class Hand is mutable hand object , we can make it ummutable hand object
by cloning it"""


import sys


class FrozenHand(Hand):

    def __init__(self, *arg, **kw):
        if len(arg) == 1 and isinstance(arg[0], Hand):
            other = arg[0]
            self.cards = other.cards
            self.dealer_card = other.dealer_card
        else:
            super().__init__(*arg, **kw)

    def __hash__(self):
        h = 0
        for c in self.cards:
            h = (h + hash(c)) % sys.hash_info.modulus
        return h

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r},{_cards_str})".format\
               (__class__ = self.__class__, n=len(repr(self.dealer_card))+9, _cards_str = ", ".join\
                (map(repr,self.cards)), **self.__dict__)
    
    


def card_from_bytes(buffer):
    string = buffer.decode("utf8")
    assert string[0] == "(" and string[-1] == ")"
    code, rank, suit = string[1:-1].split()
    class_ = {"A":AceCard, "F":FaceCard, "N":NumberCard}[code]
    rank = {"A":"1", "J":"11", "Q":"12", "K":"13"}.get(rank, int(rank))
    suit = {"Club":Club, "Diamond":Diamond, "Heart":Heart, "Spade":Spade}[suit]
    return class_(rank, suit)
    


class HandLazy(Hand):
    def __init__(self, dealer_card, *cards):
        super().__init__(dealer_card, *cards)

    @property
    def card(self):
        return self.cards

    @card.setter
    def card(self,acard):
        self.cards.append(acard)
        

            
    
