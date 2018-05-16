""" conrxt management with 'with' statement"""
import random
class Sequence:
    def __init__(self, seed=0):
        self.__seed = 0

    # defining the enter method
    def __enter__(self):
        """this method will save the previous state of the random module"""
        self.__was = random.getstate()
        random.seed(self.__seed, version=2)
        return self

    #defining exit method
    def __exit__(self, exc_type, exc_value, traceback):
        "reset the state of the random method"
        random.setstate(self.__was)
        
