import collections.abc
class power1(collections.abc.Callable):
    "create callable Power object"
    def __call__(self, x, n):
        p = 1
        for i in range(n):
            p *= x
        return p

""" using better algorithm to aim better performance """

class power2(collections.abc.Callable):
    "Callabe object  for power , run-time O(logn)"
    def __call__(self, x, n):
        if n == 0:
            return 1
        elif n % 2 ==1:
            return self.__call__(x, n-1) * x
        else: # n is even number
             t = self.__call__(x, n // 2)
             return t * t


""" using memoization """

class power3(collections.abc.Callable):
    "create callable object with cache memory"

    def __init__(self):
        self.__memory = {}

    def __call__(self, x, n):
        if (x, n) not in self.__memory:
            if n == 0:
                return 1
            elif n % 2 == 1:
                return self.__call__(x, n-1) * x
            elif n % 2 == 0:
                t = self.__call__(x, n // 2)
                self.__memory[(x, n)] = t * t
            else:
                raise Exception("Logic Error")
        return self.__memory[(x, n)]

"""callable API """
class Bet(collections.abc.Callable):
    def __init__(self):
        self._win = 0
        self._loss = 0
        self._stage = 1

    @property
    def win(self):
        return self._win

    @win.setter
    def win(self, value):
        self._win = value
        self._stage +=1

    def __call__(self):
        return self._stage

"""callable API """

class Bet2(collections.abc.Callable):
    def __init__(self):
        self.win = 0
        self.loss = 0
        self.win = 0
    def __setattr__(self, name, value):
        if name =="win":
            self.stage =1
        elif name == "loss":
            self.stage +=1
        super().__setattr__(name, value)

    def __call__(self):return self.stage
