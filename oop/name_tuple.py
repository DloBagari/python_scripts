from collections import namedtuple
blackJackCard = namedtuple("blackJackCard","rank,suit,soft,hard")


class AceCard(blackJackCard):
    __slots__ = ()

    def __new__(self,suit):
        return super().__new__(AceCard, "A",suit, 1, 11)


if __name__ == "__main__":
    a = AceCard("heart")
    print(a.suit)
    print(a.rank)
