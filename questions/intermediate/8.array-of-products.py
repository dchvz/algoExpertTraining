# Longest Peak 🔵
# Write a function that takes in a non-empty array of integers and returns an array of the products
# of all the integers in the input array except for the integer at that index.
# note, we cannot use division to solve this problem.
# For example, if our input array is [5, 1, 4, 2], our expected output would be [8, 40, 10, 20]
# because:  1 * 4 * 2 = 8, 5 * 4 * 2 = 40, 5 * 1 * 2 = 10, 5 * 1 * 4 = 20

# Time Complexity O(n)
# Space Complexity O(n)
def arrayOfProducts(array):
  products = []
  left = [1]*len(array)
  right = [1]*len(array)

  prod = 1
  for i in range(0, len(array)):
    left[i] = prod
    prod *= array[i]
  prod = 1
  for i in range(len(array)-1, -1, -1):
    right[i] = prod
    prod *= array[i]
  for i in range(0, len(array)):
    left_number = left[i]
    right_number = right[i]
    products.append(left_number * right_number)

  return products

print(arrayOfProducts([5, 1, 4, 2])) # [8, 40, 10, 20]
print(arrayOfProducts([1, 7, 3, 4])) # [84, 12, 28, 21]
print(arrayOfProducts([2, 1, 5, 3])) # [15, 30, 6, 10]
