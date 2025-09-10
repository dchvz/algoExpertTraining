# Evaluate Expression Tree 🟢
# You're given the root node of a binary tree that represents an expression. In this tree, each leaf node is an integer value, and each internal node is one of the four basic arithmetic operators: +, -, *, or /.
# Write a function that evaluates the expression represented by this tree and returns the result.
# You can assume that the tree is a valid expression tree and that division is integer division.
# To represent the operators, use the following integer values:
# Addition: -1
# Subtraction: -2
# Division: -3
# Multiplication: -4
# Sample Input:
#         -1
#        /  \
#      -2    3
#     /  \   / \
#    4    5 6  2
# Sample Output: 13
# Explanation: The expression represented by the tree is ((4 - 5) + (6 / 2)), which evaluates to 13.

# This is an input class. Do not edit.
class BinaryTree:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def evaluate_expression_tree(tree):
  result = 0
  return get_operator_sum(tree, result)

# Time Complexity O(n) where n is the number of nodes
# Space Complexity O(h) where h is the height of binary tree)
def get_operator_sum(tree, result):
  if tree is None:
    return 0

  if tree.left is None and tree.right is None:
    return tree.value

  left = get_operator_sum(tree.left, result)
  right = get_operator_sum(tree.right, result)

  if tree.value == -4:
    result += left * right
  elif tree.value == -3:
    result += int(left / right)
  elif tree.value == -2:
    result += left - right
  elif tree.value == -1:
    result += left + right

  return result

# Tree: ((4 - 5) + (6 / 2))
tree1 = BinaryTree(
  -1,
  left=BinaryTree(
    -2,
    left=BinaryTree(4),
    right=BinaryTree(5)
  ),
  right=BinaryTree(
    -3,
    left=BinaryTree(6),
    right=BinaryTree(2)
  )
)

# Tree: (7 * (3 + 2))
tree2 = BinaryTree(
  -4,
  left=BinaryTree(7),
  right=BinaryTree(
    -1,
    left=BinaryTree(3),
    right=BinaryTree(2)
  )
)

# Tree: ((10 / 2) - (8 + 1))
tree3 = BinaryTree(
  -2,
  left=BinaryTree(
    -3,
    left=BinaryTree(10),
    right=BinaryTree(2)
  ),
  right=BinaryTree(
    -1,
    left=BinaryTree(8),
    right=BinaryTree(1)
  )
)

print(evaluate_expression_tree(tree1))  # Output: 4
print(evaluate_expression_tree(tree2))  # Output: 35
print(evaluate_expression_tree(tree3))  # Output: -4