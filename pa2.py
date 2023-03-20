# File: pa2.py
# Author:     
# Date: 
# Description: Program containing a function
# to solve the problem described in pa2 for comp 480,
# spring 2023.

from rbtree import RBTree

def pa2(filename):
    """
    Solves problem described in pa2 problem statement.
    filename is the name of the file containing the input.
    Should return the result: either None
    if the problem has no solution, or a tuple containing two orders:
    the order of the first set up numbers, and the order of the second
    set of numbers.
    """


    f = open(filename, 'r')
    num_elements = int(f.readline())


    

    #set unordered list a
    unordered_list_A = []
    zero_index = f.readline().split()
    first_index = f.readline().split()
    i = 0
    tuple_place = 1
    for item in zero_index:
        unordered_list_A.append((int(item), int(first_index[i]),tuple_place))
        tuple_place+=1
        i += 1

    #set unordered list b
    unordered_list_B = []
    zero_index = f.readline().split()
    first_index = f.readline().split()
    i = 0
    tuple_place = 1
    for item in zero_index:
        unordered_list_B.append((int(item), int(first_index[i]),tuple_place))
        tuple_place+=1
        i += 1

    print("LIST A: ")
    print(unordered_list_A)
    print("LIST B: ")
    print(unordered_list_B)

    sorted_A = merge_sort(unordered_list_A)
    sorted_B = merge_sort(unordered_list_B)
    print('\n'+"SORTED LIST A: ")
    print(sorted_A)
    print('\n'+"SORTED LIST B: ")
    print(sorted_B)


    #start with a merge sort for bullet point one?

    #bullet point two might need greedy alg

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        elif left[i][0] == right[j][0]:
            if left[i][1] < right[j][1]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

if __name__ == "__main__":
    """
    Can run this file directly when testing your code.
    """
    ans = pa2("input1.txt")


