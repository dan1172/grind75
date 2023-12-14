from ast import List

# O(n^2) solution
def twoSum(nums, target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return [-1]


# O(n) solution
def twoSum(nums, target: int) -> List[int]:
    d = dict()
    for i in range(len(nums)):
        d[nums[i]] = i
    for i in range(len(nums)):
        if (target - nums[i]) in d and i != d[target - nums[i]]:
            return [i, d[target - nums[i]]]
    return [-1]