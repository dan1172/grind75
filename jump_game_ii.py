# import math


# class Solution:
#     def jump(self, nums) -> int:
#         n = len(nums)
#         nj = [math.inf] * n
#         for i in range(n):
#             if i == 0:
#                 nj[i] = 0
#                 continue
#             else:
#                 least = math.inf
#                 for j in range(i):
#                     if nums[j] + j >= i:
#                         least = min(least, nj[j] + 1)
        
#         return nj[n - 1]


class Solution:
    def jump(self, nums) -> int:
        n = len(nums)
        q = [(0, 0)]
        while q:
            (s, i) = q.pop(0)
            ns = s + 1
            if nums[i] + i >= n: return s
            for j in range(1, nums[i] + 1):
                q.append((ns, i + j))
            