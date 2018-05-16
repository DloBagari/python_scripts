from random import Random
from Card import Card
from suits import *
class Deck(list):
    def __init__(self, size=1):
        super().__init__()
        card = Card()
        suit = Suits.suits()
        self.rng = Random()
        for d in range(size):
            cards = [card(rank, s) for rank in range(1,14) for s in suit]
            self.extend(cards)
        #neccessry to turn of the class feature in the subclass
        try:
            self._init_shuffle()
        except (AttributeError, TypeError):
            pass

    def _init_shuffle(self):
        self.rng.shuffle(self)


