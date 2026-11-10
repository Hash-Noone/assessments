# QUEST 2 — Big O: Growth, Not Guesswork (25 marks)
# Learning target: Connect Python operations and loops 
# to time complexity, auxiliary space, and practical trade-offs.
# Each function checks whether a list contains a duplicate:
def has_duplicate_a(items):
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return True
    return False

def has_duplicate_b(items):
    seen = set()
    for item in items:
        if item in seen:
            return True
        seen.add(item)
    return False

def has_duplicate_c(items):
    items = sorted(items)
    for i in range(1, len(items)):
        if items[i] == items[i - 1]:
            return True
    return False
# A. Analyze (9 marks): For each implementation, 
# state the worst-case or expected time complexity as appropriate, 
# plus auxiliary space complexity. 
# Point to the operations that create that cost.

# funcA use a time complexity of O(n^2) and Space complexity of O(1) because in each iteration of a value 
# it runs throught the list again. but it only creates i and j so it is a consistent space.
# funcB use a time complexity of O(n) and Space complexity of O(n) 
# because it creates a set to store the values it has seen.
# funcC use a time complexity of O(n log n) and Space complexity of O(n) 
# because it sorts the list which takes O(n log n) and 
# creates a new sorted list which takes O(n) space.

# B. Predict before running (5 marks): 
# Compare a list of 10,000 distinct integers 
# funcA will run about 50 million times in the worst case because n = 10,000 and no duplicates.
# funcA will use a small amount of memory because it only creates i and j so it is a consistent space.
# funcB will run about 10,000 times in the worst case because n = 10,000 and no duplicates.
# funcB will use a mid amount of memory because it creates a set to store the values it has seen.
# funcC will run about 10,000 log 10,000 times in the worst case because n = 10,000 and no duplicates
# funcC will use a large amount of memory because it creates a new sorted list.

# with a list whose first two values are equal.
#funcA will run about 1 time in the worst case because n = 10,000 and the first two values are equal.
#funcA will use a small amount of memory because it only creates i and j so it is a consistent space.
#funcB will run about 2 times in the worst case because n = 10,000 and the first two values are equal.
#funcB will use a small amount of memory because it creates a set to store only the first value it has seen.
#funcC will still run about 10,000 log 10,000 times because it will sort the list first and then check for duplicates.
# funcC will use a large amount of memory because it creates a new sorted list.

# Which implementations can return early?
# funcA can return early if it finds a early duplicate in the inner loop.
# funcB will return early optimally if it finds a duplicate while iterating through the list.

# Which is likely to do the most work on distinct values?.
# funcA will do the most work on distinct values because it has to check every pair of values in the list.

# Explain why Big O is not an exact stopwatch.
# Big O always checks the worst case scenario and does not take into account the actual time it takes to run the code. 
# It is a measure of how the algorithm scales with input size, not how long it takes to run in practice.

# C. Correct the misconception (5 marks): A student says, “Implementation B is O(1) because set membership is O(1).
# While it is true that set membership is O(1), 
# the overall time complexity of Implementation B is O(n) 
# because it has to iterate through the entire list of items to check for duplicates. 
# The O(1) membership check is only a part of the overall process, 
# and since we have to do this for each item in the list, 
# the total time complexity becomes O(n).
# 
# ” Explain the difference between the expected cost of one set lookup and the cost of processing n items
# the expected cost of one set lookup is O(1) because it takes a constant amount of time to check if an item is in the set.
# The cost of processing n items is O(n) because we have to check each item in the list to see if it is a duplicate, which takes linear time.
# .
# D. Make an engineering choice (6 marks): 
# Choose an implementation for millions of records. 
# Discuss speed, memory, sorting/input mutation, and what collision-heavy hashing could mean. 
# A strong answer names a trade-off.
# The best working implementation for millions of records would be Implementation B.
# It has a time complexity of O(n) and a space complexity of O(n)
# it also doesn't require sorting or modifying the input.


# Use this reminder: Big O describes how resource use grows as input size grows; it does not promise an exact number of seconds.
# Optional self-check after completing your written analysis: test n = 10, 100, and 1,000 with both duplicate and no-duplicate cases. Record what changes and what does not.
