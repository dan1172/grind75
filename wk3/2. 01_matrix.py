class Solution:
    def updateMatrix(self, mat):
        queue = []
        m, n = len(mat), len(mat[0])
        dist = [[-1 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j, 0))
                    
        while queue:
            i, j, d = queue.pop(0) 
            if 0 <= i < m and 0 <= j < n and dist[i][j] == -1:
                dist[i][j] = d 
                queue.extend(((i + 1, j, d + 1), (i - 1, j, d + 1), (i, j + 1, d + 1), (i, j - 1, d + 1)))
        return dist
        
        
        
mat = [[0,0,0],[0,1,0],[0,0,0]]

s = Solution()
print(s.updateMatrix(mat))