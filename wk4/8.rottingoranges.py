class Solution:
    def orangesRotting(self, grid) -> int:
        mins = 0
        m = len(grid)
        n = len(grid[0])
        num_fine = 0
        r, c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num_fine += 1
                elif grid[i][j] == 2:
                    r, c = i, j

        q = [(r, c)]
        while q: 
            (r, c) = q.pop()
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                