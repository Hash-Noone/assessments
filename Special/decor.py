
def announce(func):
    # This runs once when the decorator is applied.
    print("Decorator is running")

    def wrapper(*args, **kwargs):
        # Runs before the original function.
        print("Before function")

        # Call the original function with its arguments.
        result = func(*args, **kwargs)

        # Runs after the original function completes successfully.
        print("After function")

        # Pass the original function's result back to the caller.
        return result

    # Return the wrapper to replace the original function.
    return wrapper


@announce
def multiply(a, b):
    print("Multiplying")
    return a * b


print("Program started")

answer = multiply(3, 4)

print("Answer:", answer)

# Predict Output:
# Decorator is running
# Program Started
# Before Function
# Multiplying
# After Function
# Answer:
# The reason why 'Decorator is running' is printed before
# 'Program Started' is because of the shorthand @announce which
# initializes the decorator on the multiply function, so the moment
# we call the multiply function, we automatically initiate the decorator
# function first.

# A. @announce — decorator syntax

# This is Python's shorthand for applying a callable decorator to a function. It is not exclusive to 
# decorators in the sense that closures cannot use the same behavior; decorators commonly use 
# closures to retain access to the original function.

# B. wrapper(*args, **kwargs) — the wrapper

# The inner function intercepts calls to the decorated function.
# - *args collects positional arguments into a tuple, such as 5, 6, 7.
# - **kwargs collects keyword arguments into a dictionary, such as count=5, name="Drake".
# Using both lets the wrapper support different argument combinations.

# C. func(*args, **kwargs) — call the original function

# This executes the function passed into announce, forwarding the arguments supplied by the caller.

# D. return result — preserve the result

# The wrapper must return the original function's result if callers are expected to receive that result.

# Without it, the wrapper implicitly returns None.
