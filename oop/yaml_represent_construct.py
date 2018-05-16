import yaml

class Card:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __str__(self):
        return "{0.rank!s}{0.suit!s}".format(self)
    __repr__ = __str__


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit,10, 1)


class FaceCard(Card):
    def __init__(self, rank,suit):
        super().__init__(rank, suit, 10, 10)

#build representers
def card_representer(dumper, card):
    #"!Card" is the tag
    return dumper.represent_scalar("!Card", str(card))

def acecard_representer(dumper, card):
    # we could use str(card)
    return dumper.represent_scalar("!AceCard", "{0.rank!s}{0.suit!s}".format(card))

def facecard_representer(dumper, card):
    return dumper.represent_scalar("!FaceCard", "{0.rank!s}{0.suit!s}".format(card))

#registor representers

yaml.add_representer(Card, card_representer)
yaml.add_representer(AceCard, acecard_representer)
yaml.add_representer(FaceCard, facecard_representer)

#build constructors
def card_constructor(loader, node):
    value = loader.construct_scalar(node)
    return Card(value[:-1], value[-1])

def acecard_constructor(loader, node):
    value = loader.construct_scalar(node)
    return AceCard(value[:-1], value[-1])

def facecard_constructor(loader, node):
    value = loader.construct_scalar(node)
    return FaceCard(value[:-1], value[-1])

#register constructors
yaml.add_constructor("!Card", card_constructor)
yaml.add_constructor("!AceCard", acecard_constructor)
yaml.add_constructor("!FaceCard", facecard_constructor)




if __name__ =="__main__":
    deck = [AceCard("A",'♥'), FaceCard("Q", '♣')]
    objects=yaml.dump(deck, allow_unicode=True)
    print(objects)

    deckcopy = yaml.load(objects)
    print(deckcopy)
    

    
