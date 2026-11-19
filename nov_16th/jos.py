def josephus(n, k):
    return 0 if n == 1 else (josephus(n - 1, k) + k ) % n 

print(josephus(1, 2))