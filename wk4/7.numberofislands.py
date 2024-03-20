class Solution:
    def numIslands(self, grid) -> int:
        num = 0
        n, m = len(grid), len(grid[0])
        islands = [[-1 for _ in range(n)] for _ in range(m)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and islands[i][j] == -1:
                    self.bfs(grid, islands, i, j, n, m)
                    num += 1
        return num
                
                
    def bfs(self, grid, islands, i, j, n, m):
        stack = [(i, j)]
        while stack:
            i,j = stack.pop()
            print(i, j, n, m)
            if 0 <= i < n and 0 <= j < m and grid[i][j] == "1" and islands[i][j] == -1:
                islands[i][j] = 1
                stack.extend(((i, j-1), (i, j + 1),(i -1, j),(i+1, j)))
            

print(Solution.numIslands(Solution, [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))