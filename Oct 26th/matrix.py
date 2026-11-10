a =  [[1, 2,3], [3, 4,5],[6,7,9]]
b =  [[5, 6,7], [7, 8,9],[1,2,3]]
result = []
for _ in range(len(a)):
    result.append([0] * len(b[0]))
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            result[i][j] += a[i][k] * b[k][j]
print(result)