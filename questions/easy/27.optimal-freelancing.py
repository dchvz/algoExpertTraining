# Optimal Freelancing 🟢
# You recently decided to start freelancing. You have a list of jobs that you could do, where each job has a payment amount and a deadline.
# Each job takes one full day to complete, and you can only work on a single job each day.
# Given a list of jobs, write a function that returns the maximum amount of money you can earn by the end of the week if you only work for 7 days and you can only work on a job before its deadline.
# Each job is represented as an object with a "payment" integer property and a "deadline" integer property.
# The "payment" property represents how much money you will earn upon completing the job, and the "deadline" property represents the last day you can work on the job.
## Each job will take one day to complete, and you can only work on a single job each day.

# Sample Input:
# [
#   { "payment": 1, "deadline": 1 },
#   { "payment": 2, "deadline": 1 },
#   { "payment": 2, "deadline": 2 },
# ]
# Sample Output: 3

# This solution is ideal because it takes the most profitable as close to the deadline as possible
# Time Complexity O(n), where n is the number of jobs, actually is O(d * n) where d is the number of days to work (7 in this case) but since it's a constant we can ignore it
# Space Complexity O(1)
def optimalFreelancing(jobs):
  days_to_work = 7
  max_profit = 0
  while days_to_work > 0:
    day_profit = 0
    day_index = -1
    for index, job in enumerate(jobs):
      if job["deadline"] >= days_to_work and job["payment"] > day_profit:
        day_profit = job["payment"]
        day_index = index
    if day_profit > 0:
      max_profit += day_profit
      del jobs[day_index]
    days_to_work -= 1

  return max_profit

print(optimalFreelancing([
  { "payment": 1, "deadline": 1 },
  { "payment": 2, "deadline": 1 },
  { "payment": 2, "deadline": 2 },
]))

print(optimalFreelancing([
  { "payment": 1, "deadline": 2 },
  { "payment": 2, "deadline": 2 },
  { "payment": 3, "deadline": 3 },
]))

print(optimalFreelancing([
  { "payment": 1, "deadline": 2 },
  { "payment": 2, "deadline": 2 },
  { "payment": 3, "deadline": 3 },
  { "payment": 2, "deadline": 1 },
  { "payment": 5, "deadline": 7 },
  { "payment": 3, "deadline": 6 },
]))