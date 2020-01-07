"""
This problem was asked by Google.
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right

node = Node('a', Node('c'), Node('b',Node('b'),Node('b',None,Node('b'))))

def is_unival(root):
    if root == None:
        return True
    if root.left != None: # check left value equal to root value
        if root.value != root.left.value:
            return False
    if root.right != None: # check left value equal to root value
        if root.value != root.right.value:
            return False
    if (not is_unival(root.left)) & (is_unival(root.right)): 
		# check left right subtree are unival
        return True
    return False

def count_unival_subtrees(root):
    if root == None:
        return 0
    left = count_unival_subtrees(root.left)
    right = count_unival_subtrees(root.right)
    return 1 + left + right if is_unival(root) else left + right
print(count_unival_subtrees(node))

def helper(root):
    if root == None:
        return (0,True)
    left, is_left_unival = helper(root.left) 
    right, is_right_unival = helper(root.right) 
    is_unival = True
    if (not is_left_unival) | (not is_right_unival):
        is_unival = False
    if root.left != None:
        if root.value != root.left.value:
            is_unival = False
    if root.right != None:
        if root.value != root.right.value:
            is_unival = False
    return (1+left+right,True) if is_unival else (right + left,False)

def count_unival_subtrees(root):
    count, _ = helper(root)
    return count

print(count_unival_subtrees(node))