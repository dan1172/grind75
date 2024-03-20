def findMatrix(nums):
    # count stores the occurences of each number
    count = {}
    most_occurences = 0
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
        most_occurences = max(most_occurences, count[num])
    res = [[] for _ in range(most_occurences)]
    for num, occ in count.items():
        for i in range(occ):
            res[i].append(num)
    return res

# findMatrix([1,2,3,4])

findMatrix([1,3,4,1,2,3,1])