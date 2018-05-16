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


p = power2()
    
