from contextlib import ContextDecorator
from deck import *
class TestDeck(ContextDecorator, Deck):
    def __init__(self, size=1, seed=0):
        super().__init__(size=size)
        self.seed = seed
    #turning off class feature
    _init_shuffle = None
    
    def __enter__(self):
        self.rng.seed(self.seed, version=1)
        self.rng.shuffle(self)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass
