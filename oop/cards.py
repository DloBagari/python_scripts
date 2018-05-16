import pickle
import builtins

class Cards:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return "{__class__.__name__}({rank!r}, {suit!r})".format(\
            __class__=self.__class__, rank = self.rank, suit = self.suit)
    __str__ = __repr__


class NumberCard(Cards):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)

class AceCard(Cards):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 1, 11)

class FaceCard(Cards):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 10, 10)
        

class RUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        if module == "builtins":
            if name not in ("exec", "eval"):
                return getattr(builtins, name)
        elif module == "__main__":
            #all the requested classes must be on globals()
            #for this resean they must be in this page
            return globals()[name]
        
        raise pickle.UnpicklingError("global '{module}.{name}, is forbidden"\
                                     .format(module=module, name= name))


if __name__ == "__main__":
    deck = Cards("A","a",8,8)
    with open("deck.p", "wb") as target:
        pickle.dump(deck, target)
