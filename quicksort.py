class QuickSort:
    "sorting a list using using quick sort algorthim"
    def __init__(self):
        self.__list = None

    def __call__(self,lst):
        self.__list = lst
        self.__quicksort(self.__list,0,len(self.__list) -1)
        return self.__list

    def __quicksort(self, mylist, first, last):
        #sort elements of mylist from first up to last
        if last > first:
            pivot = mylist[first]
            f = first + 1
            b = last
            while f <= b:
                while f <= b and mylist[f] <= pivot:
                    f += 1
                while f <= b and mylist[b] >= pivot:
                    b -= 1
                if f < b:
                    mylist[f], mylist[b] = mylist[b], mylist[f]
                    f += 1
                    b -= 1
            mylist[b], mylist[first] = mylist[first], mylist[b]
            self.__quicksort(mylist, first, b-1)
            self.__quicksort(mylist, b+1, last)
