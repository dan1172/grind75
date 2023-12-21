class Solution:
    def canJump(self, nums) -> bool:
        max_reachable = 0
        for i in range(len(nums)):
            if i <= max_reachable:
                max_reachable = max(max_reachable, nums[i] + i)
        return max_reachable >= len(nums) - 1
