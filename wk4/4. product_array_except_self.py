class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        roll = 1
        for i in range(len(nums)):
            if i == 0:
                res[i] = 1
            else:
                roll = roll * nums[i - 1]
                res[i] = roll
        roll = 1
        for i in range(len(nums) - 2, -1, -1):
            roll = roll * nums[i + 1]
            res[i] = roll * res[i]
        return res
