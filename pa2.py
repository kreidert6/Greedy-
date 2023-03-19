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
    for item in zero_index:
        unordered_list_A.append((int(item), int(first_index[i])))
        i += 1

    #set unordered list b
    unordered_list_B = []
    zero_index = f.readline().split()
    first_index = f.readline().split()
    i = 0
    for item in zero_index:
        unordered_list_B.append((int(item), int(first_index[i])))
        i += 1

    print("LIST A: ")
    print(unordered_list_A)
    print("LIST B: ")
    print(unordered_list_B)


    #start with a merge sort for bullet point one?

    #bullet point two might need greedy alg


if __name__ == "__main__":
    """
    Can run this file directly when testing your code.
    """
    ans = pa2("input1.txt")