class HeapSort:

    def __init__(self):
        self.__heap = None
        self.__lst = None

    def __call__(self, lst):
        self.__heap = []
        self.__lst = lst
        self.__buildHeap()
        return self.__sort()

    def __heappush(self,item):
        self.__heap.append(item)
        self.__bubble_up(len(self.__heap ) -1)

    def __heappop(self):
        if self.__heap:
            
            lastItem = self.__heap.pop()
            if self.__heap:
                item = self.__heap[0]
                self.__heap[0] = lastItem
                self.__bubble_down()
                return item
            else:
                return lastItem
            

    def __bubble_up(self, end, start=0):
        heap = self.__heap
        item = heap[end]
        while start < end:
            parentIndex = (end -1) //2
            parent = heap[parentIndex]
            if parent > item:
                heap[end] = parent
                end = parentIndex
                continue
            break
        heap[end] = item

    def __bubble_down(self,start=0):
        heap = self.__heap
        end = len(heap)
        item = heap[start]
        childIndex = start * 2 + 1
        while childIndex < end:
            rightChildIndex = childIndex + 1
            if rightChildIndex < end and  \
               heap[childIndex] > heap[rightChildIndex]:
               childIndex = rightChildIndex
            heap[start] = heap[childIndex]
            start = childIndex
            childIndex = start * 2 + 1
        heap[start] = item
        self.__bubble_up(len(heap) - 1)

    def __buildHeap(self):
        for item in self.__lst:
            self.__heappush(item)
            
    def show(self):
        print(self.__heap)

    def __sort(self):
        lst_sorted = []
        for i in range(len(self.__heap)):
            lst_sorted.append(self.__heappop())
        return lst_sorted
