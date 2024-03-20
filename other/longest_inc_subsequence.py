def lengthOfLIS(nums) -> int:
    dp = [-1] * len(nums)
    dp[0] = 1
    for i in range(1, len(nums)):
        best = 0
        for j in range(0, i):
            if nums[j] < nums[i]:
                best = max(best, dp[j])
        dp[i] = best + 1
    return max(dp)
        
        
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
x = [1,2,3,4,5,6,7]
# print(x[:1])