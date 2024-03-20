# Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

# Example 1:

# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.



class Solution:
    def canPartition(self, nums) -> bool:
        total = 0
        for n in nums:
            total += n
            
        if total % 2 == 1:
            return False

        target = n / 2
        
        # now, is it psosible to make the total with any numbers of nums
        
        # p[i][j] = True when it is possible to sum to j using num[i] and up to num[i]
        p = [[False for _ in range(len(nums))] for _ in range(target + 1)] 
        
        for i in range(len(nums)):
            for j in range(len(target + 1)):
                
        
        
        return
    
    