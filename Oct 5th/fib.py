from functools import lru_cache

def memoize(func):
    mem = {}
    def wrapper(*args):
        if args in mem:
            return mem[args]
        result = func(*args)
        mem[args] = result
        return result
    return wrapper
@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# def MinCost(n, cost, mem):
#     if n in mem:
#         return mem[n]
#     else:
#         mem[n] = cost[n] + min(MinCost(n + 1, cost, mem) if n + 1 < len(cost) else 0, MinCost(n + 2, cost, mem) if n + 2 < len(cost) else 0)
#         return mem[n]


# cost = [10, 15, 20]
# mem = { len(cost): 0, }
# lowest = min(MinCost(0, cost, mem), MinCost(1, cost, mem))
print(fib(80))