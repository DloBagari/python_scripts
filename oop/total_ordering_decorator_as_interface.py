"""the decorator is works like interface in java but not excatly
the class must have the __eq__ , and one of the other comarsion methods defined
the decorator will create the missing comparsion methods
"""
import functools


@functools.total_ordering
class Card:
    __slots__ = ("__rank", "__suit")

    def __new__(cls, rank, suit):
        self = super().__new__(cls)
        self.__rank = rank
        self.__suit = suit
        return self

    def __eq__(self, other):
        return self.__rank == other.__rank and self.__suit == other.__suit

    def __lt__(self, other):
        return self.__rank < other.__rank
