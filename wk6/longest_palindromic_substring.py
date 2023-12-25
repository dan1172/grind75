class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = (-1, -1)
        for i in range(1,len(s)):
            for j in range(i):
                lo, hi = j, i
                valid = True
                while lo < hi:
                    if s[lo] != s[hi]:
                        valid = False
                    lo += 1
                    hi -= 1 
                print(f"{s[j:(i+1)]} is {valid}")
                print(f"{j} {i} : {s[j:(i+1)]} is {valid}")
                if valid and i - j + 1 > best[1] - best[0]:
                    best = (j, i)
                    
        return s[j:i]