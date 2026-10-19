matrix = [[2, 4, 6], 
          [1, 3, 5], 
          [10, 20, 30]]
count = 1
col_sum = [0] * len(matrix[0])
for row in matrix:
    row_total = 0
    for index, col in enumerate(row):
        row_total += col
        col_sum[index] += row[index]
    print(f"Row {count} total: {row_total} | Row {count} average: {row_total/len(row)}")
    count += 1

print()

count = 1
for num in col_sum:
    print(f"Column {count} total: {num}")
    count += 1