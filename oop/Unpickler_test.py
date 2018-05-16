from random import randint
import pickle
from cards import AceCard

if __name__ == "__main__":
    deck = [1,2]
    with open("deck.p", "wb") as target:
        pickle.dump(deck, target)
