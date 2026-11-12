def pascal_rows(n):
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        previous = triangle[-1]
        row = [1]

        for j in range(1, len(previous)):
            row.append(previous[j - 1] + previous[j])

        row.append(1)
        triangle.append(row)

    return triangle

def pascal_row(k):
    if k < 0:
        return []

    row = [1]

    for _ in range(k):
        row.append(1)

        for j in range(len(row) - 2, 0, -1):
            row[j] += row[j - 1]

    return row

def print_rows(triangle):

    for i, row in enumerate(triangle):
        spaces = " " * (len(triangle) - i - 1)
        print(spaces + " ".join(map(str, row)))


tests = [
    (0, []),
    (1, [[1]]),
    (2, [[1], [1, 1]]),
    (5, [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ])
]

for n, expected in tests:
    assert pascal_rows(n) == expected

for k in range(5):
    assert pascal_row(k) == pascal_rows(k + 1)[-1]

print("All tests passed!")