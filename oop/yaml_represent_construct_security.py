import yaml

class Card(yaml.YAMLObject):
    yaml_tag = "!Card"
    yaml_loader = yaml.SafeLoader
    
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __str__(self):
        return "{0.rank!s}{0.suit!s}".format(self)
    __repr__ = __str__


class AceCard(Card):
    yaml_tag = "!AceCard"
    
    def __init__(self, rank, suit):
        super().__init__(rank, suit,10, 1)


class FaceCard(Card):
    yaml_tag = "!FaceCard"
    
    def __init__(self, rank,suit):
        super().__init__(rank, suit, 10, 10)




if __name__ =="__main__":
    deck = [FaceCard("Q", '♣'), AceCard("A",'♥')]
    objects=yaml.dump(deck, allow_unicode=True, explicit_end=True)
    print(objects)
    deckcopy = yaml.safe_load(objects)
    print(deckcopy)

    

    
