import sys

def missing_number(n,data):
    return n * (n + 1) // 2 - sum(data)

data = list(map(int, sys.stdin.read().split()))


print(missing_number(data[0], data[1:]))