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





