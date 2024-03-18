def do(grid):
    q = []
    dist = 0
    nr = 0

    m, n = len(grid), len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                grid[i][j] = 1
                nr += 1
                q.append(((i, j, -1)))
            elif grid[i][j] == 1:
                nr += 1

    while q:
        i, j, d = q.pop()
        if 0 <= i < m and 0 <= j < n and grid[i][j] == 1:
            q.extend(((i, j + 1, d + 1), (i, j - 1, d + 1), (i - 1, j, d + 1), (i + 1, j, d + 1)))
            grid[i][j] = 2
            nr -= 1
            dist = max(dist, d)

    return dist if nr == 0 else -1


grid = [[[0,2]]]
do(grid)
print(do(grid))
