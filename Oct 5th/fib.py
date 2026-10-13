def fib(n, mem = None):
    if mem == None:
        mem = {}
    if n < 2:
        return n
    if n in mem:
        return mem[n]
    mem[n] = fib(n - 1, mem) + fib(n - 2, mem)
    return mem[n]

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