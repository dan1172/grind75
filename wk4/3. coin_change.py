class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        dp = [float ('INF') for _ in range(amount + 1)]
        dp[0] = 0
        
        for target in range(1, len(dp)):
            for coin in coins:
                if target - coin >= 0:
                    dp[target] = min(dp[target], dp[target - coin] + 1)
    
        if dp[amount] == float ('INF'): 
            return -1
        else:
            return  dp[amount]
    
    
s = Solution()
print(s.coinChange([1,2,5], 9))