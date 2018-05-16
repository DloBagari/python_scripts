from copy import deepcopy
class MergeSort:
    def __int__(self):
        self.__list = None

    def __call__(self, lst):
        self.__list = lst
        lst_copy = deepcopy(self.__list)
        self.__sort_recursion(lst_copy, self.__list, 0, len(self.__list))
        return self.__list

    def __sort_recursion(self, copy, orginal, start, end):
        # sort copy 'list' from range 'start' up to 'end' , and insert the result into 'orginal'
        length = end - start
        # base cases  to terminate recursion.
        if length <= 2:
            if length == 2:
                if orginal[start] > orginal[start + 1]:
                    # swap  values
                    orginal[start] , orginal[start + 1] = orginal[start + 1] , orginal[start]
            return
        # find the position of the middle item in the list 'orginal' 
        divider = (start + end) //2
        #sort the first half of the list 'orginal' and put the result in the list 'copy'
        self.__sort_recursion(orginal, copy, start, divider)
        #sort the second half of the list 'orginal' and put the result in the list 'copy'
        self.__sort_recursion(orginal, copy, divider, end)
        # inserting the items by order from first half and the second half of the list 'copy' into list 'orginal
        left = start
        right = divider
        position = start
        while position < end:
            if right == end or ( left < divider and copy[left] < copy[right]):
                orginal[position] = copy[left]
                left += 1
            else:
                orginal[position] = copy[right]
                right += 1
            position += 1
        
        
