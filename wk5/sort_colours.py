class Solution:
    def sortColors(self, nums) -> None:
        ok = False
        while not ok:
            ok = True
            for i in range(len(nums) - 1):
                if nums[i + 1] < nums[i]:
                    ok = False
                    temp = nums[i]
                    nums[i] = nums[i + 1]
                    nums[i + 1] = temp
        """
        Do not return anything, modify nums in-place instead.
        """
        