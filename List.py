class AVLTreeList(object):
    def __init__(self):
        self.clear()

    def clear(self):
        self.root =AVLTreeList.Node.EMPTY_LEAF_NODE
    def __len__(self):
        return self.root.size
    def empty_node(self):
        return self.Node(None, True)

    def insert(self, index, val):
        if index < 0 or index > len(self):
            raise IndexError()
        self.root = self.root.insert_at(index, val)

    def append(self, value):
        self.insert(len(self), value)

    def __setitem__(self, index, value):
        " updating exist index's value"
        if index < 0 or index >= len(self):
            raise IndexError()
        self.root.get_node_at(index).value = value

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("assigned index is out of the range")
        return self.root.get_node_at(index).value

    def __delitem__(self, index):
        "deleting item from the tree"
        if index <0 or index >= len(self):
            raise IndexError("giving index is out of the range")
        self.root = self.root.remove_at(index)
        
    def pop(self, index = None):
        "delete and return the last item if index is None"
        index = index or len(self)-1
        if index <0 or index >= len(self):
            raise IndexError("pop index is out of the range of the tree indexs")
        collected = self.__getitem__(index)
        self.__delitem__(index)
        return collected 

    def check_structure(self):
        return self.root.check_structure(set())
         

    def __iter__(self):
        return AVLTreeList.Iter(self)

    def __str__(self):
        #return "["+", ".join(str(i) for i in self)+"]"
        return "["+", ".join(str(self[i]) for i in range(len(self)))+"]"
        
    def display(self):
        self.root._display()
    
            

    class Node(object):
        def __init__(self, val, isleaf=False):
            self.value = val
            """case one : node will be a leaf , no left or right child
            in this case the height is zero since there is nothing ander this
            node , and the size is the number of node in the subtree where
            this node is a root, the number of node include node itself"""
            if isleaf:
                self.height = 0
                self.size = 0
                self.left = None
                self.right = None
                """case two: if the node is going to be not a leaf , which will havea
               left, right child , in this case height will be 1, and size will be 1
               and left and right child will be tree with empty node"""
            else:
                self.height = 1
                self.size = 1
                self.left = AVLTreeList.Node.EMPTY_LEAF_NODE
                self.right = AVLTreeList.Node.EMPTY_LEAF_NODE

        def insert_at(self,index, obj):
            try:
                assert 0 <= index <= self.size
                if self is AVLTreeList.Node.EMPTY_LEAF_NODE:
                    if index == 0:
                        return AVLTreeList.Node(obj)
                    else:
                        raise IndexError()
                leftsize = self.left.size
                if index <= leftsize:
                    self.left = self.left.insert_at(index, obj)
                else:
                    self.right = self.right.insert_at(index - leftsize-1, obj)
                self._recalculate()
                return self._rebalance()
            except IndexError:
                print("error: index is out of range")

        def get_node_at(self, index):
            "finding the reponding index node"
            if self is AVLTreeList.Node.EMPTY_LEAF_NODE:
                raise ValueError()
            leftsize = self.left.size
            if index < leftsize:
                return self.left.get_node_at(index)
            elif index > leftsize:
                return self.right.get_node_at(index - leftsize - 1)
            else:
                return self

        def _recalculate(self):
            "recalculate the height and size of the Node"
            assert self is not AVLTreeList.Node.EMPTY_LEAF_NODE
            assert self.left.height >= 0 and self.right.height >= 0
            assert self.left.size >= 0 and self.right.size >=0
            self.height = 1 + max(self.left.height, self.right.height)
            self.size = self.left.size + self.right.size + 1
            assert self.height >= 0 and self.size >= 0

        def _get_balance(self):
            "the deffer between right_height and left_height"
            return self.right.height - self.left.height

        def _rebalance(self):
            balance = self._get_balance()
            assert abs(balance) <= 2
            result = self
            if balance == -2:
                assert abs(self.left._get_balance()) <= 1
                if self.left._get_balance() == +1:
                    self.left = self.left._rotate_left()
                result = self._rotate_right()
            elif balance == +2:
                assert abs(self.right._get_balance()) <= +1
                if self.right._get_balance() == -1:
                    self.right = self.right._rotate_right()
                result = self._rotate_left()
            assert abs(result._get_balance()) <= 1
            return result

        def _rotate_left(self):
            " from right to left rotation"
            assert self is not AVLTreeList.Node.EMPTY_LEAF_NODE
            root = self.right
            self.right = root.left
            root.left = self
            self._recalculate()
            root._recalculate()
            return root

        def _rotate_right(self):
            "from left to right rotation"
            assert self.left is not AVLTreeList.Node.EMPTY_LEAF_NODE
            root = self.left
            self.left = root.right
            root.right = self
            self._recalculate()
            root._recalculate()
            return root

        def remove_at(self, index):
            empty = AVLTreeList.Node.EMPTY_LEAF_NODE
            if self is empty:
                raise ValueError()
            leftsize = self.left.size
            if index < leftsize:
                self.left = self.left.remove_at(index)
            elif index > leftsize:
                self.right = self.right.remove_at(index - leftsize - 1)
            elif self.left is empty and self.right is empty:
                return empty
            elif self.left is empty and self.right is not empty:
                return self.right
            elif self.left is not empty and self.right is empty:
                return self.left
            else:
                self.value = self._get_successor()
                self.right = self.right.remove_at(0)
            self._recalculate()
            return self._rebalance()

        def _get_successor(self):
            "exchanging the value of removing index with the next index's value"
            empty = AVLTreeList.Node.EMPTY_LEAF_NODE
            if self is empty or self.right is empty:
                raise ValueError()
            node = self.right
            while node.left is not empty:
                node = node.left
            return node.value

        def __str__(self):
            return "AVLTreeList( size = {}, height = {}, value = {})".\
                   format(self.size, self.height, self.value)

        def __len__(self):
            return self.size

        def check_structure(self,visited):
            if self is  AVLTreeList.Node.EMPTY_LEAF_NODE:
                return
            if self in visited:
                raise AssertionError(" avl tree sturcture : not a tree")
            visited.add(self)
            self.left.check_structure(visited)
            self.right.check_structure(visited)
            if self.height != max(self.left.height, self.right.height) + 1:
                raise AssertionError("avl structure: incurrect catched height")
            if self.size != self.left.size + self.right.size + 1:
                raise AssertionError("avl structure: incurrect catched size")
            if abs(self._get_balance()) > 1:
                raise AssertionError("avl strcture : height imbalnace")

        def _display(self, level=0):
            """ when we ckeck the condition  if self.vale  this will return
              false when the value is one of (None, 0 , false ) or any falsey
              value, but  in our case in there if we declate a value for the node
              than the node's value should be vaild except if the value is None
              for this resean we have to ckeck if self.value is not None only"""
            if self is AVLTreeList.Node.EMPTY_LEAF_NODE:
                raise Exception("this tree is empty")
            if self.right.value is not None:
                self.right._display(level + 1)
                print ('\t' * level, '   /')
        
            print ('\t' * level, self.value)
 
            if self.left.value is not None:
             
                print ('\t' * level, '   \\')
                self.left._display(level + 1)


    class Iter(object):
        def __init__(self, outer):
            self.stack = AVLTreeList()
            node = outer.root
            while node is not AVLTreeList.Node.EMPTY_LEAF_NODE:
                self.stack.append(node)
                node = node.left

        def __next__(self):  #python 3

             if len(self.stack) == 0:
                 raise StopIteration
             else:
                 node = self.stack.pop()
                 result = node.value
                 node = node.right
                 while node is not AVLTreeList.Node.EMPTY_LEAF_NODE:
                     self.stack.append(node)
                     node = node.left
                 return result
        next = __next__ # python 2

         

AVLTreeList.Node.EMPTY_LEAF_NODE = AVLTreeList.Node(None, True)

from time import time
def compare():
    t = AVLTreeList()
    now = time()
    for i in range(10000):
        t.append(i)

