# Minimum Waiting Time 🟢
# Write a function that returns the minimum amount of total waiting time for all queries.
# Sample Input [3,2,1,2,6]
# Sample Output 17

# Time Complexity O(nlogn) because sorting is necessary on the queries array
# Space Complexity O(1) because we use single variables to keep track of data
def minimum_waiting_time(queries):
  # sorting is necessary to prevent executing longer queries first
  queries.sort()
  iteration_wait_time = 0
  overall_wait_time = 0
  prev_query_wait_time = 0

  for query in queries:
    iteration_wait_time = iteration_wait_time + prev_query_wait_time
    overall_wait_time = iteration_wait_time + overall_wait_time
    prev_query_wait_time = query

  return overall_wait_time

print(minimum_waiting_time([3,2,1,2,6]))
print(minimum_waiting_time([1,1,1,1,1]))
print(minimum_waiting_time([25,30,2,1]))
