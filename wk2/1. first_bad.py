# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo = 1
        hi = n
        while (lo <= hi):
            mid = (hi + lo) // 2
            if (lo == hi):
                return lo
            elif (isBadVersion(mid)):
                # if the curr one is bad, we don't care about any bad one after it
                hi = mid
            else:
                # if the curr one is good, then we know that we should only care about anyhting 
                lo = mid + 1
        return -1  
    
    
    # 1 good
    # 2 good 
    # 3 good 
    # 4 bad 
    # 5 bad