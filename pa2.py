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
    unordered_list_A = getUnorderedList(f)

    #set unordered list b
    unordered_list_B = getUnorderedList(f)

    #Create trees ordered by first element
    tree_a = RBTree(key = lambda x: x[0])
    for item in unordered_list_A:
        tree_a.insert(item)

    tree_b = RBTree(key = lambda x: x[0])
    for item in unordered_list_B:
        tree_b.insert(item)

    second_num_dict_A = createSecondNumDict(unordered_list_A)
    second_num_dict_B = createSecondNumDict(unordered_list_B)


    final_list_A = []
    final_list_B = []

    for i in range(len(tree_a)):
        switch = False
        min_a = tree_a.delete_min()
        min_b = tree_b.delete_min()
        len_a_tree = len(second_num_dict_A[min_a[0]])
        len_b_tree = len(second_num_dict_B[min_b[0]])

        if(len_a_tree>=len_b_tree):
            try:
                new_b_node = second_num_dict_B[min_b[0]].delete_min()
                new_compare_a_val = second_num_dict_A[min_a[0]].delete_smallest_greater_than(new_b_node)
                final_list_A.append(new_compare_a_val)
                final_list_B.append(new_b_node)
            except:
                return None
        else:
            try:
                new_a_node = second_num_dict_A[min_a[0]].delete_min()
                new_compare_b_val = second_num_dict_B[min_b[0]].delete_largest_less_than(new_a_node)
                final_list_A.append(new_a_node)
                final_list_B.append(new_compare_b_val)
            except:
                return None

    final_output = getFinalOutput(final_list_A,final_list_B)

    return final_output


def createSecondNumDict(unordered_list):
    second_num_dict = {}
    for item in unordered_list:
        try:
            second_num_dict[item[0]].insert(item)
        except KeyError:
            tree = RBTree(key = lambda item: item[1])
            second_num_dict[item[0]] = tree
            second_num_dict[item[0]].insert(item)
    return second_num_dict


def getUnorderedList(f):
    unordered_list = []
    zero_index = f.readline().split()
    first_index = f.readline().split()
    i = 0
    tuple_place = 1
    for item in zero_index:
        unordered_list.append((int(item), int(first_index[i]),tuple_place))
        tuple_place+=1
        i += 1
    return unordered_list

def getFinalOutput(list_a,list_b):
    final_indexes_a = []
    final_indexes_b = []
    for i in range(len(list_a)):
        final_indexes_a.append(list_a[i][2])
        final_indexes_b.append(list_b[i][2])
    return (final_indexes_a,final_indexes_b)


if __name__ == "__main__":
    """
    Can run this file directly when testing your code.
    """
    ans = pa2("input8.txt")
    print(ans)


