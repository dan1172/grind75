class Solution:
    def updateMatrix(self, mat):
        m = len(mat)
        n = len(mat[0])
        #res = [[-1] * m] * n
        res = [[0 for i in range(m)] for j in range(n)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                else:
                    res[i][j] = self.bfs(i, j, mat)
        return res
                    
        
    def bfs(self, x, y, mat):
        m = len(mat)
        n = len(mat[0])
        q = [(x, y, 0)]
        visited = [[-1] * m] * n
        while q:
            (x, y, d) = q.pop(0)
            if 0 <= x < m and 0 <= y < n and visited[x][y] == -1:
                visited[x][y] = 1
                if mat[x][y] == 0:
                    return d
                nd = d + 1
                q.extend([(x + 1, y, nd), (x - 1, y, nd),(x, y + 1, nd),(x, y - 1, nd)])