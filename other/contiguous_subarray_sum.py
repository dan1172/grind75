class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        n = len(nums)
        for i in range(2, n):
            