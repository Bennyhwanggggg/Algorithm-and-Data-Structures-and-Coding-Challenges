# Generates a binary tree T whose shape is random and whose nodes store
# random even positive integers, both random processes being directed by user input.
# With M being the maximum sum of the nodes along one of T's branches, minimally expands T
# to a tree T* such that:
# - every inner node in T* has two children, and
# - the sum of the nodes along all of T*'s branches is equal to M.
#
# Written by Benny Hwang 12/10/2017


import sys
from random import seed, randrange

from binary_tree_adt import *


def create_tree(tree, for_growth, bound):
    if randrange(max(for_growth, 1)):
        tree.value = 2 * randrange(bound + 1)
        tree.left_node = BinaryTree()
        tree.right_node = BinaryTree()
        create_tree(tree.left_node, for_growth - 1, bound)
        create_tree(tree.right_node, for_growth - 1, bound)

path = []
def expand_tree(tree):
    if tree.value is None:
        return tree
    
    path.append(tree.value)
    diff = max_sum - sum(path)
    
    if tree.left_node.value is not None:
        expand_tree(tree.left_node)
    else:
        if diff != 0:
            tree.left_node.insert_in_bst(diff)
    if tree.right_node.value is not None:
        expand_tree(tree.right_node)
    else:
        if diff != 0:
            tree.right_node.insert_in_bst(diff)
    path.pop()
    
def max_sum_of_branch(tree):
    if tree.value is None:
        return tree
    
    leftSum = False
    rightSum = False
    # if we have reached end of the tree
    if tree.right_node.value is None and tree.left_node.value is None:
        return tree.value
    else:
        # i it has children, we calculate sum of each branch
        if tree.left_node.value is not None:
            leftSum = max_sum_of_branch(tree.left_node)
        if tree.right_node.value is not None:
            rightSum = max_sum_of_branch(tree.right_node)
        # find maximum
        if leftSum and rightSum:
            if leftSum > rightSum:
                return tree.value + leftSum
            else:
                return tree.value + rightSum
        elif leftSum:
            return tree.value + leftSum
        else:
            return tree.value + rightSum
        
try:
    for_seed, for_growth, bound = [int(x) for x in input('Enter three positive integers: ').split()
                                   ]
    if for_seed < 0 or for_growth < 0 or bound < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
 
seed(for_seed)
tree = BinaryTree()
create_tree(tree, for_growth, bound)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
max_sum = max_sum_of_branch(tree)
expand_tree(tree)
print('Here is the expanded tree:')
tree.print_binary_tree()




