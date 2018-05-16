from collections import deque
from random import shuffle
import timeit

class FastPop(deque):
    def __init__(self, size=1):
        super().__init__()
        for i in range(size):
            numbers = list(range(10000))
            super().extend(numbers)
        #shuffle(self)

if __name__ == "__main__":
    print(timeit.timeit("x.pop()","""
from list_to_deque_fast_pop import FastPop
x =FastPop()""", number = 10000))
    print(timeit.timeit("x.pop()","x =list(range(10000))""", number = 1000))


"""as we see the deque is faster the list in pop operation"""
