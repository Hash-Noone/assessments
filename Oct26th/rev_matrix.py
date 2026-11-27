matrix = [
[1,2],
[3,4],
]
# result = []
# for nums in zip(*matrix):
#     temp = []
#     for num in nums:
#         temp.insert(0, num)
#     result.append(temp)
for i in range(len(matrix)):
    for j in range(i+1,len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
print(str(matrix)[1:-1].replace("], ", "]\n").replace(",",""),sep="\n")
print()

for i in range(len(matrix)):
    for j in range(len(matrix[0])//2):
        matrix[i][j], matrix[i][len(matrix)-j-1] = matrix[i][len(matrix)-j-1], matrix[i][j]

print(str(matrix)[1:-1].replace("], ", "]\n").replace(",",""),sep="\n")
