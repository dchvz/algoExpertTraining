# 🟦 Find Successor
# Write a function that takes in a Binary Tree and a node contained in that tree and returns the given node's successor.
# A node's successor is the next node to be visited (immediately after the given node) when traversing its tree using the in-order tree-traversal technique.
# Each BinaryTree node has an integer value, a left child node, a right child node, and a parent node.
# If a node has no successor, your function should return None / null.
# A node is said to be a valid BinaryTree node if and only if it satisfies the BinaryTree property where its children nodes are either valid BinaryTree nodes themselves or None / null.
# Sample Input
# tree =    1
#           / \
#          2   3
#         / \ / \
#        4  5 6  7
#       / \
#      8  9
# node = 5
# Sample Output
# 6

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Time Complexity O(n) where n is the number of nodes
# Space Complexity O(n)
def findSuccessor(tree, node):
    array = []
    helper(tree, node, array)
    successor = None
    for index, element in enumerate(array):
        if element.value == node.value:
            nextElement = array[index + 1] if index + 1 < len(array) else None
            successor = nextElement
            break
    return successor

def helper(tree, node, array):
    if tree is None:
        return

    helper(tree.left, node, array)
    array.append(tree)
    helper(tree.right, node, array)

