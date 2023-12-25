class Solution:
    def minOperations(self, s: str) -> int:
        c1, c2 = 0, 0
        # c1 = 0101010101010..., c2 = 101010101010.....
        # c1 expects 0 on even indexes, and 1 on odd indexes
        # cs expects 1 on even indexes, and 0 on odd indexes
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] == '0':
                    c2 += 1
                else:
                    c1 += 1
            else:
                if s[i] == '0':
                    c1 += 1
                else:
                    c2 += 1
        return min(c1, c2)