import math

class Solution:
    def longestPalindrome(self, s: str) -> int:
        table = {}
        mid_filled = False
        size = 0
        for c in s:
            if c in table.keys(): 
                table[c] = table[c] + 1
            else:
                table[c] = 1
        for n in table.values():
            if n % 2 == 0: 
                # can add all of them
                size = size + n
            elif not mid_filled: 
                # can addd all of them asw
                size = size + n
                mid_filled = True 
            else: 
                # can add all but one
                size = size + n - 1
        return size