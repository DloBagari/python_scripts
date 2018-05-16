#!/usr/bin/env python
#--------------------------------------------------------------------------
#sort.py
#
#sorting a list of integers in Python
#
# Date: 20-05-2013
# Tested with Python3
# TO RUN:
#         sudo chmod a+x sort.py
#         ./sort.py
# OR JUST RUN : python3 sort.py
#
# @Author: Dlo Jiwan Bagari
# @id 114702261
# ---------------------------------------------------------------------------
from sys import exit
from random import randint
def get_list():
    #get user input and convert it to a list of numbers
    try:
        numbers = input()
        return [int(item) for item in numbers.strip().split()]
    except ValueError:
        exit()

a = [randint(1,100000) for _ in range(10000000)]
def sort(my_list):
    # sorting the list in place and return it.

    # create copy of the orginal list
    alias = my_list[:]
    
    sort_recursion(alias, my_list, 0, len(my_list))
    return my_list
    
def sort_recursion(copy, orginal, start, end):
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
    sort_recursion(orginal, copy, start, divider)
    #sort the second half of the list 'orginal' and put the result in the list 'copy'
    sort_recursion(orginal, copy, divider, end)
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


sort([randint(1,10000000) for _ in range(100000)])
