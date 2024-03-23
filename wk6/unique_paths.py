class Solution:
    def uniquePaths(self, m: int, n: int):
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                if i == 0 or j == 0:
                    continue
                dp[i][j] = dp[i][j - 1] + dp[i-1][j]
        
        return dp[i][j]