def total(n):
    if not isinstance(n,int):
        raise TypeError("Enter an integer")
    if n < 0:
        raise ValueError("Enter a positive number")
    if n < 1:
        return 0
    if n == 1:
        return 1
    return n + total(n - 1)
#print(total(4))
# Tracing total(4).
# This simple becomes 4 + total(3): 
# which becomes 3 + total(2): 
# which 2 + total(1): 
# which becomes 1 because it is a base case
# back to 2 + 1
# back to 3 + 2 + 1
# bacl to 4 + 3 + 2 + 1 
# = 10.

# B. Find the problem (5 marks): What happens for total(0) and total(-3)
# There is no base cases for float numbers or number less than 1?
# It runs into maximum recursive depth exceeded

# C. Explain termination (5 marks):
# This is having a base case and a recursive case that moves towards that base case
# And must trigger the base case if it doesnt then there is no termination. 

# distinguish the base case from the recursive case.

# Base case is the situation which your recursive function stops calling 
# it self/ make new calls and the previous calls finish.

# recursive case is how the function keeps making new calls of itself to solve the 
# problem in bits 

# Explain why each call must move toward a stopping condition
# Each new call should move towards your base case or stopping condition 
# because thats what stops our recursive function from making new calls 
# and enter an infinite amount of call.

# What failure occurs if the stopping condition is never reached?
# It runs into maximum recursive depth exceeded.
#
#  D. Code it (5 marks): Write countdown_sum(n), 
# which recursively returns the sum of odd positive integers from n down to 1. 
# Return 0 for n <= 0. Do not use loops, sum(), count(), or comprehensions.
def countdown_sum(n):
    if not isinstance(n,int):
        raise TypeError("Enter an integer")
    return 0 if n <= 0 else countdown_sum(n - 1) if n % 2 == 0 else  n + countdown_sum(n - 2)
    
    
# Examples:
print(countdown_sum(10))  # 9: 5 + 3 + 1
print(countdown_sum(4))  # 4: 3 + 1
print(countdown_sum(1))  # 1
print(countdown_sum(0))  # 0
# Python learning note: A recursive call is an ordinary function call. Each call has its own argument values and waits for the next call to return.
