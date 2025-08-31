# Product Sum 🟢
# Write a function that takes in a special array and returns its product sum
# A special array is the sum of its elements where special arrays inside it are summed themselves, and then multiplied by their depth
# The product sum of [x+y] is x+y; the product sum of [x, [y, z]] is x + 2 * (y + z); the product sum of [x, [y, [z]]] is x + 2 * (y + 3 * z)
# Sample Input: [5,2,[7,-1],3,[6,[-13,8],4]]
# Sample Output: 12


def product_sum(array):
  return get_inner_array_sum(array, 1, 1)

# Time Complexity O(n) where n is all the elements and sum elements
# Space Complexity O(d) where d is the maximum depth of the nested arrays
# Note: The space complexity is due to the recursive calls
def get_inner_array_sum(array, overall_depth, current_depth):
  sum = 0
  for item in array:
    if isinstance(item, int):
      sum += item*overall_depth
    else:
      sum += get_inner_array_sum(item, (current_depth + 1)*overall_depth, current_depth + 1)
  return sum

# this is the solution proposed in the video explanation, it resolves the problem more easily
# it shows how to avoid passing the overall depth and current depth
def elegant_get_inner_array_sum(array, multiplier):
  sum = 0
  for item in array:
    if isinstance(item, int):
      sum += item
    else:
      sum += elegant_get_inner_array_sum(item, multiplier + 1)
  return sum*multiplier

print(product_sum([5,2,[7,-1],3,[6,[-13,8],4]]))
print(product_sum([
    [
      [
        [
          [5]
        ]
      ]
    ]
  ]))