def sumOfUnique(nums) -> int:
    d = {}
    res = 0
    for n in nums:
        if n in d:
            d[n] += 1
        else:
            d[n] = 1
    for k, v in d.items():
        if v == 1:
            res += k
    return res

print(sumOfUnique([1,2,3,2]))