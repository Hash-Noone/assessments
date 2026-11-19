def weird(n):
    result = [str(n)]
    while n != 1:
        n = n // 2 if n % 2 == 0 else n * 3 + 1
        result.append(str(n))
    return " ".join(result)

print(weird(int(input())))