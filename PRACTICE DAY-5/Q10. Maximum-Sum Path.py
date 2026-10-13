matrix = [
    [1, 3, 1],
    [2, 5, 2],
    [4, 2, 1]
]
rows = len(matrix)
cols = len(matrix[0])
dp = [[0] * cols for _ in range(rows)]
path = [[None] * cols for _ in range(rows)]
dp[0][0] = matrix[0][0]
for i in range(1, rows):
    dp[i][0] = dp[i-1][0] + matrix[i][0]
    path[i][0] = (i-1, 0)
for j in range(1, cols):
    dp[0][j] = dp[0][j-1] + matrix[0][j]
    path[0][j] = (0, j-1)
for i in range(1, rows):
    for j in range(1, cols):
        if dp[i-1][j] > dp[i][j-1]:
            dp[i][j] = dp[i-1][j] + matrix[i][j]
            path[i][j] = (i-1, j)
        else:
            dp[i][j] = dp[i][j-1] + matrix[i][j]
            path[i][j] = (i, j-1)
i, j = rows-1, cols-1
result = []
while True:
    result.append(matrix[i][j])
    if i == 0 and j == 0:
        break
    i, j = path[i][j]
result.reverse()
print("Maximum path sum:", dp[rows-1][cols-1])
print("Path:", result)
