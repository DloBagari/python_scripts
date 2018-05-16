class Node:

    def __init__(self, index=None, value=None, before=None, after=None, demo=False):
        if demo :
            self._before = None
            self._after = None   
        else:
            self._before = before
            self._after = after
            self._value = value
            self._index = index


class Link:

    def __init__(self):
        self._tail = Node(demo=True)
        self._head = Node(demo=True)
        self._tail._before = self._head
        self._head._after = self._tail
        self._cursor = None
        self._size = 0

    def __setitem__(self, index, value):
        """Store item at position index in
           raise IndexError if index is >= the length of the DLL
           """
        if type(index) != int or index < 0 or index >self._size:
            raise IndexError("index is out ot the range")  
        elif index == self._size:
            node = self._tail._before
            node._after = Node(index,value,node,node._after)
            self._tail._before = node._after
            self._size += 1
            if index ==0:
                self._cursor = self._head._after
        else:
            self._find(index)._value = value      

    def append(self, value):
        self.__setitem__(self._size, value)

    def insert(self,index, value):
        self.__setitem__(index, value)

    def __getitem__(self,index):
        """Return the item at position index
        raise IndexError if index is >= the length of the DLL
        """
        if type(index) != int or index <0 or index >=self._size:
            raise IndexError("index out of the range")
        return self._find(index)._value
        
    def _find(self,index):
        node = self._head._after
        while True:
            if node._index == index:
                break
            node = node._after
        return node

    def __iter__(self):
        node = self._head._after
        while node != self._tail:
            yield node._value
            node= node._after
        raise StopIteration

    def is_empty(self):
        return self._size == 0


    def next_node(self):
        if self._cursor != self._tail:
            node = self._cursor
            self._cursor = self._cursor._after
            return node._value
        return "end"



class Level(Link):
    def __init__(self, quantum, timeSlice):
        super().__init__()
        self.__quantum = quantum
        self.__timeSlice = timeSlice

    def pr(self):
        return (self.__quantum, self.__timeSlice)
        
