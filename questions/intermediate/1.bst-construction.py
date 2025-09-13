# BST Construction 🔵
# Write a BST class for a Binary Search Tree. The class should support:
# Insertion of values with the insert method.
# Searching for values with the contains method.
# Removal of values with the remove method.
# The remove method should only remove the first instance of a given value.
# You should not remove values from a single-node tree. In other words, calling the remove
# method on a single-node tree should simply not do anything.
# Each BST node has an integer value, a left child node, and a right child node.
# A node is said to be a valid BST node if and only if it satisfies the BST property:
# its value is strictly greater than the values of every node to its left;
# its value is less than or equal to the values of every node to its right;
# and its children nodes are either valid BST nodes themselves or None / null.
# Note that you will not be able to remove values from a single-node tree. In other
# words, calling the remove method on a single-node tree should simply not do anything.

# Average for all three methods
# Time Complexity O(logn)
# Space Complexity O(1) where n is the number of nodes in the BST
class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    currentNode = self
    while True:
      if value < currentNode.value:
        if currentNode.left:
          currentNode = currentNode.left
        else:
          currentNode.left = BST(value)
        break
      else:
        if currentNode.right:
          currentNode = currentNode.right
        else:
          currentNode.right = BST(value)
        break
    return self

  def contains(self, value):
      currentNode = self
      while currentNode is not None:
        print(currentNode.value, value)
        if currentNode.value == value:
          return True
        elif currentNode.value > value:
          currentNode = currentNode.left
        else:
          currentNode = currentNode.right
      return False

  def remove(self, value, parentNode = None):
      currentNode = self
      while currentNode is not None:
        if value < currentNode.value:
          parentNode = currentNode
          currentNode = currentNode.left
        elif value > currentNode.value:
          parentNode = currentNode
          currentNode = currentNode.right
        else:
          if currentNode.left is not None and currentNode.right is not None:
            currentNode.value = currentNode.right.getMinValue()
            currentNode.right.remove(currentNode.value, currentNode)
          elif parentNode is None:
            if currentNode.left is not None:
              currentNode.value = currentNode.left.value
              currentNode.right = currentNode.left.right
              currentNode.left = currentNode.left.left
            elif currentNode.right is not None:
              currentNode.value = currentNode.right.value
              currentNode.left = currentNode.right.left
              currentNode.right = currentNode.right.right

          elif parentNode.left == currentNode:
            parentNode.left = currentNode.left if currentNode.left is not None else currentNode.right

          elif parentNode.right == currentNode:
            parentNode.right = currentNode.left if currentNode.left is not None else currentNode.right

          break
      return self

  def getMinValue(self):
    currentNode = self
    while currentNode.left is not None:
      currentNode = currentNode.left
    return currentNode.value





