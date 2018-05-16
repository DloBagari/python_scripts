class Suits:
    def __init__(self):
        pass
    @staticmethod
    def suits():
        Club, Diamond, Heart, Spade = Suit('Club','♣'),Suit('Diamond','♦'),\
                              Suit('Heart','♥'), Suit('Spade','♠')
        return [Club, Diamond, Heart, Spade]

class Suit:
    def __init__(self,name,symbol):
        self.name = name
        self.symbol = symbol

    def __str__(self):
        return self.symbol

    __repr__ = __str__
