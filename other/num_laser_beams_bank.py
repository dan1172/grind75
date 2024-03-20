def numberOfBeams(bank) -> int:
    # Find first row with something
    i = 0
    while i < len(bank):
        prev = bank[i].count('1')
        if prev != 0:
            break
        i += 1
    if i == len(bank) - 1:
        return 0
    res = 0
    for i in range(i + 1, len(bank)):
        cur = bank[i].count('1')
        if cur == 0:
            continue
        else:
            res += prev * cur
            prev = cur
    return res

print(numberOfBeams(["011001","000000","010100","001000"]))