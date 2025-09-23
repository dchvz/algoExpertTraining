# BST Traversal 🔵
# Write three functions that take in a binary search tree (BST) and return an array of its values in:
# in-order traversal
# pre-order traversal
# post-order traversal

# Time Complexity O(n): where n is the number of nodes in the tree
# Space Complexity O(n): where n is the number of nodes in the tree
def in_order_traverse(tree, array):
  if tree is None:
    return

  in_order_traverse(tree.left, array)
  array.append(tree.value)
  in_order_traverse(tree.right, array)

  return array

def pre_order_traverse(tree, array):
  if tree is None:
    return
  array.append(tree.value)

  pre_order_traverse(tree.left, array)
  pre_order_traverse(tree.right, array)

  return array


def post_order_traverse(tree, array):
  if tree is None:
    return

  post_order_traverse(tree.left, array)
  post_order_traverse(tree.right, array)

  array.append(tree.value)

  return array
