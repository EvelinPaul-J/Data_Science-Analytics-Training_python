matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
n = len(matrix)
result = []
for j in range(n):
    row = []
    for i in range(n-1, -1, -1):
        row.append(matrix[i][j])
    result.append(row)
for row in result:
    print(*row)
