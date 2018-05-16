from cards import *

class Card:
    def __init__(self):
        pass
    def __call__(self, rank, suit):
        if rank == 1 :
            return AceCard("A",suit)
        elif 2 <= rank < 11:
            return NumberCard(str(rank), suit)
        elif 11 <= rank <14:
            name = {11:"J", 12:"Q", 13:"K"}[rank]
            return FaceCard(name, suit)
        else:
            raise Exception("range out of range") 
    
        
