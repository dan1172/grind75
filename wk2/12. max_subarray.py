import math

class Solution:
    def maxSubArray(self, nums):
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[0]
            else:
                dp[i] = max(nums[i], nums[i] + dp[i -1])
        return max(dp)