def pascal_triangle(n):
    def pascal(n, triangle = [[1]], mem = None):
    if n <= 0:
        return []
    if n == 1:
        return triangle
    if mem is None:
        mem = {}
    if n in mem:
        return mem[n]
    last_row = triangle[-1]
    new_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
    triangle.append(new_row)
    mem[n] = triangle
    return pascal(n - 1, triangle, mem)


    