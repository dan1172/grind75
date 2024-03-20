class Solution:
    def search(self, nums, target: int) -> int:
        lo, hi = 0, len(nums) -1
        while lo <= hi:
            mid = (lo + hi) // 2
            print("querying index", mid)
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target: # queried element is too big
                # if the target is less than the last element, then search to the right
                if target < nums[len(nums) - 1]:
                    lo = mid + 1
                # otheerwise search to the left
                    hi = mid - 1
            if nums[mid] < target: # queried element is too small
                
            else:
                return -1
            
        return -1
    
s = Solution()
nums =[4,5,6,7,0,1,2]
target = 0 
print(s.search(nums, target))