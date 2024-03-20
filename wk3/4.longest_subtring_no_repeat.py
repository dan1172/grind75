class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 1
        n = len(s)
        best = 1
        set = set()
        while i < n:
            j = j + 1
        return best