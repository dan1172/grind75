class Solution:
    def findAnagrams(self, s: str, p: str):
        
        if len(p) > len(s): return []
        p_occ = {}
        for c in p:
            p_occ[c] = p_occ.get(c, 0) + 1
            
         
        s_occ = {}
        for i in range(len(p)):
            s_occ[c] = s_occ.get(c, 0) + 1
        
        lo, hi = 0, len(p)
        
        while hi < len(s):
            # check if is anagram
            if 
            
            hi += 1
            lo += 1
            