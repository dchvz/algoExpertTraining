# [1, 2, 5, 7, 10, 13, 14, 15, 22]
# First Middle Value (0, 8) -> mid=4 (value=10)
# Left side: (0, 3) → mid=1 (value=2).
    # Its left: (0, 0) → mid=0 (value=1).
    # Its right: (2, 3) → mid=2 (value=5).
    # Right again: (3, 3) → mid=3 (value=7).
# Right side: (5, 8) → mid=6 (value=14).
    # Its left: (5, 5) → mid=5 (value=13).
    # Its right: (7, 8) → mid=7 (value=15).
    # Right again: (8, 8) → mid=8 (value=22).

# Time Complexity O(n)
# Space Complexity O(n)
def minHeightBst(array):
  return constructMinHeightBst(array, 0, len(array) -1)

def constructMinHeightBst(array, startIndex, endIndex):
  if endIndex < startIndex:
    return None
  midIndex = (startIndex + endIndex) // 2
  bst = BST(array[midIndex])
  bst.left = constructMinHeightBst(array, startIndex, midIndex - 1)
  bst.right = constructMinHeightBst(array, midIndex + 1, endIndex)
  return bst

class BST:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

