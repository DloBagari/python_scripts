class List:
    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__height = None
        self.__balance = 0

    def __setitem__(self, pos, value):
        if pos < 0 or pos > len(self):
            raise IndexError("postion is out of range..")
        if self.__root == None and self.__size == 0:
            self.__root = Node( value)
        else:
            self.__root = self.__root.insert(self.__root,pos, value)
            #self.__root.__parent = None
        self.__size,self.__height,self.__balance = self.__root.getsize()
        

    def __len__(self):
        if self.__root:
            return self.__size
        else:
            return 0

    def display(self):
        self.__root.display(self.__root)

    def rep(self):
        print(self.__balance,self.__height , self.__size)


        


class Node:
    def __init__(self, value):
        self.__value = value
        self.__size = 1
        self.__height = 1
        self.__left = None
        self.__right =None
        self.__parent = None

    def insert(self, node, pos, value):
        return node.__insert_at(pos, value)

    def __insert_at(self, pos, value):
        if self.__left is None and self.__size > pos:
            self.__left = Node(value)
            self.__left.__parent = self
            self.__count()
            return self
        elif self.__right is None and self.__size <= pos:
            self.__right = Node(value)
            self.__right.__parent = self
            self.__count()
            return self
        leftsize = self.__left.__size if self.__left else 0   
        if leftsize >= pos:
            self.__left = self.__left.__insert_at(pos, value)
        else:
            self.__right = self.__right.__insert_at(pos - leftsize -1, value)
        self.__count()
        return self.__balance()

    def display(self, node):
        node.__display()

    def __display(self,level=0):
        if self is None:
            raise IndexError("the list is empty")
        if self.__right:
            self.__right.__display(level=level+1)
            print("\t" * level, "  /")
        print("\t" * level,self.__value)
        if self.__left:
            print("\t" * level, "  \\")
            self.__left.__display(level=level+1)


    def __count(self):
        if self.__left == self.__right == None:
            self.__size = 1
            self.__height =0
        elif self.__left and not self.__right:
            self.__size = self.__left.__size + 1
            self.__height = self.__left.__height + 1
        elif not self.__left and self.__right:
            self.__size = self.__right.__size + 1
            self.__height = self.__right.__height + 1
        else:
            self.__size = self.__left.__size + self.__right.__size + 1
            self.__height = max(self.__left.__height, self.__right.__height) + 1

    def getsize(self):
        return self.__size, self.__height,self.__get_balance()

    def __get_balance(self):
        if self.__left == self.__right == None:
            return 0
        elif self.__left and self.__right is None:
            
            return -self.__left.__height
        elif self.__left is None and self.__right:
            return self.__right.__height
        else:
            return self.__right.__height - self.__left.__height

    def __balance(self):
        balance = self.__get_balance()
        #assert abs(balance) <=1
        result = self
        if balance == -2:
            assert abs(self.__left.__get_balance()) <= 1
            if self.__left.__get_balance() == 1 and self.__left.__right:
                self.__left = self.__left.__rotate_left()
            result = self.__rotate_right()
        elif balance == +2:
            assert abs(self.__right.__get_balance()) <= 1
            if self.__right.__get_balance() == -1 and self.__right.__left:
                self.__right = self.__right.__rotate_right()
            result = self.__rotate_left()
        #assert abs(result.__get_balance()) <= 1
        return result

    def __rotate_left(self):
        assert self.__right is not None
        root = self.__right
        self.__right = root.__left
        root.__left = self
        self.__count()
        root.__count()
        return root

    def __rotate_right(self):
        assert self.__left is not None
        root = self.__left
        self.__left = root.__right
        root.__right = self
        self.__count()
        root.__count()
        return root

@profile
def compare():
    t = List()
    for i in range(1000):
        t[i]=i

compare()        
            
        
        
        
