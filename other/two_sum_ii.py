class Solution:
    def twoSum(self, numbers, target: int):
        lo, hi = 0, len(numbers) - 1
        while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return [lo + 1, hi + 1]
            elif numbers[lo] + numbers[hi] > target:
                hi = hi - 1
            else:
                lo = lo + 1
                