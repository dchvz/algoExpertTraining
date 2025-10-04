# 🟦 Invert Binary Tree
# Write a function that takes in a binary tree and inverts it. In other words,
# the function should swap every left node in the tree for its corresponding right node.
# Each BinaryTree node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BinaryTree node if and only if it satisfies the BinaryTree property where its children nodes are either valid BinaryTree nodes themselves or None / null.
# Sample Input
# tree =    1
#           / \
#          2   3
#         / \ / \
#        4  5 6  7
#
# Sample Output
# tree =    1
#           / \
#          3   2
#         / \ / \
#        7  6 5  4

def invertBinaryTree(tree):
  invertHelper(tree)
  return tree

# Time Complexity O(n) where n is the number of nodes
# Space Complexity O(h) where h is the height of the tree
def invertHelper(node):
  if node is None:
    return

  left_node = node.left
  right_node = node.right
  node.left = right_node
  node.right = left_node

  invertHelper(node.left)
  invertHelper(node.right)

# This is the class of the input binary tree.
class BinaryTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
