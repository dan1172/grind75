class Solution:
    # def majorityElement(self, nums):
    #     list = nums.sort()
    #     n = len(nums)
    #     cur = 0
    #     for i in range(len(nums)):
    #         if i == 1: 
    #             cur = 1
    #         if nums[i] == nums[i - 1]:
    #             cur = cur + 1
    #         else: 
    #             cur = 1
    #         if cur > n // 2: 
    #             return nums[i]
    #     return -1
    def majorityElement(self, nums):
        dict = {}
        for num in nums:
            if num in dict.keys():
                dict[num] = dict[num] + 1
            else:
                dict[num] = 1
        for index, value in enumerate(dict):
            if value > len(nums) // 2:
                return index
        return -1