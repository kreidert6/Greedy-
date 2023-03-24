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

    #get return tuple of trees
    trees_return_a = getTrees(f)
    trees_return_b = getTrees(f)

    #get main trees from above tuple
    tree_a = trees_return_a[0]
    tree_b = trees_return_b[0]

    #get dict of trees from above tuple
    second_num_dict_A = trees_return_a[1]
    second_num_dict_B = trees_return_b[1]

    #final list of tuples to be added to each iteration
    final_list_A = []
    final_list_B = []

    for i in range(len(tree_a)):
        #grab the minimum first index from each tree
        min_a = tree_a.delete_min()
        min_b = tree_b.delete_min()
        len_a_tree = len(second_num_dict_A[min_a[0]])
        len_b_tree = len(second_num_dict_B[min_b[0]])

        if(len_a_tree>=len_b_tree):
            try:
                #grab smallest b node based on second num dict
                new_b_node = second_num_dict_B[min_b[0]].delete_min()
                #grabs best a tuple based on above choice
                new_compare_a_val = second_num_dict_A[min_a[0]].delete_smallest_greater_than(new_b_node)
                #append both tuples to final lists
                final_list_A.append(new_compare_a_val)
                final_list_B.append(new_b_node)
            except:
                #if the methods raise key error there is no possible choice and return None
                return None
        else:
            try:
                #grab smalled a node based on second num dict
                new_a_node = second_num_dict_A[min_a[0]].delete_min()
                #grab best b tuple based on above choice
                new_compare_b_val = second_num_dict_B[min_b[0]].delete_largest_less_than(new_a_node)
                #appened both tuples to final lists
                final_list_A.append(new_a_node)
                final_list_B.append(new_compare_b_val)
            except:
                #if the methods raise key error there is no possible choice and return None
                return None

    #convert to permutation
    final_output = getFinalOutput(final_list_A,final_list_B)

    return final_output

def getTrees(f):
    #Get Trees returns a tuple where index 0 of the return is the tree for the input (sorted on index 0 of the input tuple). 
    #   Index 1 of the return is a dictonary of trees where the key is index 0 of the input tuple and the value
    #   is a tree (sorted on index 1 of the input tuple) of all tuples with that same index 0.
    #This method will be called twice...once for list a and once for list b

    #create the tree on index 0 of the input tuples
    tree = RBTree(key = lambda x: x[0])  
    second_num_dict = {}

    #first index of 
    zero_indexes = f.readline().split()
    first_indexes = f.readline().split()
    #i value created to index into first_indexes list while iterating over zero_indexes
    i = 0
    #keep track of original tuple place
    tuple_place = 1
    for item in zero_indexes:
        tuple_to_add = (int(item), int(first_indexes[i]),tuple_place)
        tree.insert(tuple_to_add)
        tuple_place+=1
        i += 1
        #do a try except look to determine whether there is a tree already created for index 0 of this tuple. 
        #   If exists-->add. else-->create tree and add
        try:
            second_num_dict[tuple_to_add[0]].insert(tuple_to_add)
        except KeyError:
            dict_tree = RBTree(key = lambda x: x[1])
            second_num_dict[tuple_to_add[0]] = dict_tree
            second_num_dict[tuple_to_add[0]].insert(tuple_to_add)
    return (tree,second_num_dict)

def getFinalOutput(list_a,list_b):
    #iterates over the final lists and puts indexes into lists
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


