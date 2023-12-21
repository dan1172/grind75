import math

def bin_search(nums, target, lo, hi):
    mid = math.floor((lo + hi) / 2)
    if lo > hi:
        return -1
    elif nums[mid] > target:
        return bin_search(nums, target, lo, mid - 1)
    elif nums[mid] < target:
        return bin_search(nums, target, mid + 1, hi)
    else:
        return mid


class Solution:
    def search(self, nums, target: int) -> int:
        return bin_search(nums, target, 0, len(nums) - 1)
