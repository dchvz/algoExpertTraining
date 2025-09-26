# Validate BST 🔵
# Write a function that takes in a potentially invalid Binary Search Tree (BST) and returns a boolean
# representing whether the BST is valid.
# A valid BST is defined as a binary tree in which for every node, its value is strictly greater than the values of every node to its left;
# its value is less than or equal to the values of every node to its right;
# and its children nodes are either valid BSTs themselves or None / null.
# Sample Input
# tree =    10
#         /    \
#        5      15
#      /  \    /  \
#     2    5  13   22
#   /  \
#  1    3
# Sample Output
# true

# This is an input class. Do not edit.
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def validateBst(tree):
  return validationHelper(tree, float('-inf'), float('inf'))

# Time Complexity O(n) where n is the number of nodes in the tree
# Space Complexity O(d) where d is the depth of the tree
def validationHelper(tree, minValue, maxValue):
  # any node with a None value is valid BST
  if tree is None:
    return True

  # we know that every element to the left has to be strictly less than the current tree value
  # we know that every element to the right has to be strictly equal or larger than current tree value
  # if any of those conditions break, it is not a BST
  if tree.value < minValue or tree.value >= maxValue:
    return False

  # on the left subtree the min value is negative infinity, while the max value is the current tree value
  leftIsValid = validationHelper(tree.left, minValue, tree.value)
  # on the right subtree the max value is infinity, while the min value is the current tree value
  rightIsValid = validationHelper(tree.right, tree.value, maxValue)

  return leftIsValid and rightIsValid




