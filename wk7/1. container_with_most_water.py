# Below here is the naive O(n^2) soln that get's TLE
# class Solution:
#     def maxArea(self, height) -> int:
#         biggest = 0
#         for hi in range(len(height)):
#             for lo in range(hi):
#                 area = (hi - lo) * min(height[lo], height[hi])
#                 biggest = max(area, biggest)
#         return biggest

# DP attempt, well really just a bit of early exit
class Solution:
    def maxArea(self, height) -> int:
        dp = [0] * len(height)
        
        return 1
    
# two pointer soln
class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        n = len(height)
        lo, hi = 0, n - 1
        while lo < hi:            
            cur_area = (hi - lo) * min(height[lo], height[hi])
            max_area = max(max_area, cur_area)
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return max_area
    
    
# area between any two lines at i and j
# will be |(i - j)| * (min(height[i], height[j]))


# earlier and higher == defs better all the time than something
# later and shorter as our left beam we choose

# how do we decide if it would mean less width, but more height