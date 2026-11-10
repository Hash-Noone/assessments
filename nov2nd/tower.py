def hanoi(n, source = "A", target = "C", helper = "B"):
    if n == 1:
        return [(source, target)]
    moves = hanoi(n - 1, source, helper, target)
    moves += [(source, target)]
    moves += hanoi(n - 1, helper, target, source)
    return moves
print(hanoi(3))