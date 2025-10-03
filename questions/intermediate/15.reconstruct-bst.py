# 🟦 Reconstruct BST
# The pre-order traversal of a binary search tree (BST) is given as an array of integers. Write a function that reconstructs the tree represented by this pre-order traversal array. The function should return the root of the reconstructed BST.
# You can assume that there will be no duplicate values in the BST.
# Each BST node has an integer value, a left child node, and a right child node. A node is said to be a valid BST node if and only if it satisfies the BST property where its value is strictly greater than the values of every node to its left; its value is less than or equal to the values of every node to its right; and its children nodes are either valid BST nodes themselves or None / null.
# Sample Input
# preOrderTraversalValues = [10, 4, 2, 1, 5, 17, 19, 18]
# Sample Output
#         10
#        /  \
#       4    17
#      / \     \
#     2   5     19
#    /         /
#   1         18

# 10,4,2,1,5,17,19,18
# add 10
# all elements to the left are 4,2,1,5
# all elements to the right are 17, 19 ,18
# assign to the left [4,2,1,5]
# assign 4 to the left
# all elements to the left [2,1]
# all elements to the right [5]
# assign 2 to the left
# all elements to the left [1]
# assign 1 to the left
# no elements to the left/right, return root which is 1 at this point
# when 2 is assigned, no elements to the right, return root which is 2 at this point
# when 4 is assigned...
# assign 5 to the right
# no elements to the left or right, return root which is 5 at that point
# when 10 is assigned...
# [17,19,18]
# assign 17 to the right
# elements to the left []
# elements to the right [18,19]
# assign 18 to the right
# elements to the left []
# elements to the right
# assign 19 to the right
# no elements ot the left or right, return root which is 19 at this point
# recursion is done


# This is an input class. Do not edit.
class BST:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

# Time Complexity O(nlogn) where n is the numbers in the array, because we still have to go through all elements in the bst
# Space Complexity O(nlogn) because we append values in arrays at each level in the binary tree
def reconstruct_bst(traversal_values):
  tree = BST(traversal_values[0])
  left = []
  right = []
  for number in traversal_values[1:]:
    if number < tree.value:
      left.append(number)
    else:
      right.append(number)
  if left:
    tree.left = reconstruct_bst(left)
  if right:
    tree.right = reconstruct_bst(right)
  return tree
