def minOperations(nums) -> int:
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    res = 0
    for o in d.values():
        if o == 1:
            return -1
        else:
            if o % 3 == 0:
                res += o // 3
            else:
                res += o // 3 + 1
    return res

print(minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12])) #expect 7


# for any number, n, what is the least x + y, such that 3x + 2y = n

# print(minOperations([2,1,2,2,3,3]))

