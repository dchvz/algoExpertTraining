# 🟦 Find Kth Largest Value
# Write a function that takes in a Binary Search Tree (BST) and a positive integer k and returns the kth largest value in the BST. You can assume that there will only be integer values in the BST and that k is less than or equal to the number of nodes in the tree.
# Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property where its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.
# Sample Input
# tree =    15
#           /  \
#          10   20
#         / \   / \
#        8  12 17 25
#       / \
#      6   9
# k = 3
# Sample Output
# 17 // The 3rd largest value in the BST is 17.

# This is an input class. Do not edit.
class BST:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# O(n) time | O(n) space
def find_kth_largest_value(tree, k):
  nodes = []
  get_array_of_elements(tree, nodes)
  kth_position = len(nodes) - k
  return nodes[kth_position]

def get_array_of_elements(tree, array):
  if tree is None:
    return
  get_array_of_elements(tree.left, array)
  array.append(tree.value)
  get_array_of_elements(tree.right, array)
  return array





