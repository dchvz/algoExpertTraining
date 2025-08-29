# Nth Fibonacci 🟢
# The Fibonacci sequence is defined as follows:
# F(1) = 0, F(2) = 1
# F(n) = F(n - 1) + F(n - 2) for n > 2
# Write a function that returns the nth Fibonacci number.

# Time Complexity O(n) where n is the value of n
# Space complexity O(1)
def get_nth_fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    last_fibonacci = 1
    second_to_last_fibonacci = 0
    for i in range(3, n + 1):
        current_fibonacci = second_to_last_fibonacci + last_fibonacci
        second_to_last_fibonacci = last_fibonacci
        last_fibonacci = current_fibonacci
    return last_fibonacci

print(get_nth_fibonacci(6))
print(get_nth_fibonacci(7))
print(get_nth_fibonacci(14))