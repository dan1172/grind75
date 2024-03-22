class Solution:
    def longestPalindrome(self, s: str) -> str:
        # we want the lognest palindromic substring
        
        # we have O(n^3) brute force solution that
        # considers all O(n^2) possible substrings and 
        # verifies their palindromic nature in O(n)
        
        # so we have some overlapping work
        
        # key observations for recursion
            # we can see that you can easily build up the strings with one extra char and
            # be able to ensure if they're palindromes or ntot
        return ""