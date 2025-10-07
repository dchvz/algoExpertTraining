# 🟦 Binary Tree Diameter
# Write a function that takes in a binary tree and returns its diameter.
# The diameter of a binary tree is defined as the length of its longest path,
# even if that path doesn't pass through the root of the tree.
# The length of a path between two nodes is represented by the number of edges between them.
# Each BinaryTree node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BinaryTree node if and only if it satisfies the BinaryTree property where its children nodes are either valid BinaryTree nodes themselves or None / null.
# Sample Input
# tree =    1
#           / \
#          2   3
#         / \ / \
#        4  5 6  7
#       / \
#      8  9
# Sample Output
# 5 // 8 -> 4 -> 2 -> 1 -> 3 -> 6

# This is an input class. Do not edit.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# Time Complexity O(n) where n is the number of nodes
# Space Complexity O(h) where h is the height of the tree
# Used global to keep track of longest path, numbers in Python are immutable! That took me a while to figure out
# Another alternative would be to return a tuple with the longest path and height or something else
def binary_tree_diameter(tree):
  global path
  path = 0
  get_longest_path(tree)
  return path

def get_longest_path(tree):
  global path
  if tree is None:
      return 0

  left = get_longest_path(tree.left)
  right = get_longest_path(tree.right)

  curr_longest = left + right
  path = max(curr_longest, path)

  return 1 + max(left, right)