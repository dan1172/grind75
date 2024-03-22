class Solution:
    def canPartition(self, nums) -> bool:
        target = sum(nums)

        
        if target % 2 == 1: 
            return False
        target = target // 2
        # print(target)
        
        dp = [[False for _ in range(len(nums))] for _ in range(target + 1)]
        
        
        # base case, always possible to reach val 0 because simply use no values
        for j in range(len(nums)):
            dp[0][j] = True
            
        for i in range(target + 1):
            for j in range(len(nums)):
                if i - nums[j] >= 0 and j - 1 >= 0:
                    dp[i][j] = dp[i - nums[j]][j - 1]
                if i - nums[j] == 0:
                    dp[i][j] = True
                if j != 0:
                    dp[i][j] = dp[i][j] or dp[i][j - 1]
        
        res = False
        for i in range(len(nums)):
            res = res or dp[target][i]

        # for debug
        for i in range(target + 1):
            print(f"target = {i}", end = ": ")
            for j in range(len(nums)):
                print(dp[i][j], end = " ")
            print()
        return res
    
s = Solution()
# nums = [1,2,3, 2]
# nums = [14,9,8,4,3,2]
nums = [1,5,8]
# nums = [1,5,11,5]
print(s.canPartition(nums))
