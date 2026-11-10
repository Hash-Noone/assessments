def matrix_row_and_col_checker(matrix):
    return (
        "Invalid matrix"
        if not isinstance(matrix, list)
        or not (matrix and matrix[0])
        or (matrix and not all(isinstance(row, list) and len(row) == len(matrix[0]) for row in matrix))
        else (len(matrix), len(matrix[0]) if matrix else 0)
    )

def transpose_matrix(matrix):
    result = [[0] * len(matrix) for _ in matrix[0]]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            result[col][row] = matrix[row][col]
    return result

print(matrix_row_and_col_checker([[],[]]))