class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        return 1

def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    return 1


# 1 <= s.length <= 100
# 0 <= k <= s.length

# s = "aaabcccd", k = 2
# s = "a3bc2d"
# delete 'b and 'd'
# "a3c2" --> ans = 4

# s = "aabbaa", k = 2
# delete "bb"
# s = "a4"

# s = "aaaaaaaaaaa", k = 0
# delte none
# s = "a11"