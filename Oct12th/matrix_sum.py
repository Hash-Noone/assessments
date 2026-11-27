matrix = [[2, 4, 6], [1, 3, 5], [10, 20, 30]]
count = 1
for row in matrix:
    row_total = 0
    for col in row:
        row_total += col
    print(f"Row {count} total: {row_total}")
    count += 1