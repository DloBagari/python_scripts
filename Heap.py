class Heap:
    "create A heapq instance"
    def __init__(self):
        self.__heap = []

    def __len__(self):
        return len(self.__heap)

    def add(self, node):
        self.__heap.append(node)
        self.__rebuild_add(self.__heap,len(self)-1)

    def __rebuild_add(self,heap, pos, startpos=0):
        "bubble up the minimun value after adding a value"
        newitem = heap[pos]
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if parent.getWeight() > newitem.getWeight():
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    def mini(self):
        "return minimun value in the heap"
        result = self.__heap[0]
        last = self.__heap.pop()
        self.__heap[0] = last
        self.__rebuild_del(self.__heap)
        return result

    def __rebuild_del(self,heap):
        newitem = heap[0]
        pos = 0
        endpos = len(self)
        childpos = pos * 2 + 1
        while childpos < endpos:
            rightchild = childpos + 1
            if rightchild < endpos and not heap[childpos].getWeight() < \
               heap[rightchild].getWeight():
                childpos = rightchild
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = pos * 2 + 1
        heap[pos] = newitem
        self.__rebuild_add(heap,pos)

    def showheap(self):
        return [i.getWeight() for i in self.__heap]
                
        
        
        



def MakeHeap(values):
    """build a heap tree, every parent is at least as large as its childern"""

    for i in range(len(values)):
        indx = i
        while indx !=0:
            parent = (indx - 1)//2
            if values[indx] <= values[parent]:
                break
            values[indx], values[parent] = values[parent], values[indx]
            indx = parent

def RemoveTopItem(values):
    count = len(values) 
    """ remove the root item, which is the largest item in array"""
    result = values[0]

    "move last item to top to be a root"
    values[0] = values[count-1]
    

    "restore heap property"
    indx = 0
    while True:
        "find the child indices"
        child1 = 2 * indx + 1
        child2 = 2 * indx + 2

        "if the child index is off the end of the tree, use the parent's index"
        if child1 >= count:
            child1 = indx
        if child2 >= count:
            child2 = indx

        "if the heap property is satisfied, so break"
        if values[indx] >= values[child1] and values[indx] >= values[child2]:
            break

        "get the index of the child with laergest value"
        swap_child=None
        if values[child1] > values[child2]:
            swap_child = child1
        else:
            swap_child = child2
        values[swap_child], values[indx] = values[indx], values[swap_child]
    return result


"""try heapreplace(data,n),nlargest(how_many,data),nsmallest(how_many,data)
     heappushpop(data,item)"""
def HeapSort(values):
    MakeHeap(values)
    lst=[]
    """if we do range(4,0,-1) this will return i as 4,3,2,1 zero not included"""
    for i in range(len(values),0,-1):
        values[0],values[i-1] = values[i-1], values[0]
        lst.append(RemoveTopItem(values))
    return lst

    

"""using the heapq module to sort with heap"""
from heapq import heappop,heappush,heapify

def HeapSort2(values):
    """if the data are not in the memeory we use this"""
    h=[]
    for value in values:
        heappush(h,value)
    return [heappop(h) for _ in range(len(h))]
        

def HeapSort3(values):
    "if the data is oready in the memory"
    
    heapify(values)
    lst = [heappop(values) for _ in range(len(values))]


from time import time
from random import randint
def compare():
    n = 100
    while n<500000:
        a=[randint(1,n) for _ in range(n)]
        a2=a[:]
        a3=a[:]
        now = time()
        HeapSort(a)
        done1=time() - now
        now= time()
        HeapSort2(a2)
        done2=time() - now
        now = time()
        HeapSort3(a3)
        done3 = time() - now
        print(done1*1000,"       ",done2*1000,"      ",done3*1000)
        n=n*5
        
