class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            lo, hi = 0, len(nums) - 1
            while lo < hi:
                sum = nums[lo] + nums[hi] + nums[i]
                if lo == i:
                    lo += 1
                    continue
                elif hi == i:
                    hi -= 1
                    continue
                elif hi == 1:
                    hi -= 1
                elif sum == 0:
                    if not sorted([nums[i], nums[hi], nums[lo]]) in res:
                        res.append(sorted([nums[i], nums[hi], nums[lo]]))
                    lo += 1
                    hi -= 1
                elif sum > 0:
                    hi -= 1
                else:
                    lo += 1
        return res
        
        
# naive solution: sort, then 


# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]


# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.


# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105