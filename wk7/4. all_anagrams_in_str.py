class Solution:
    def findAnagrams(self, s: str, p: str):
        res = []
        if len(p) > len(s): return res
        p_occ = {}
        for c in p:
            p_occ[c] = p_occ.get(c, 0) + 1
            
         
        s_occ = {}
        for i in range(len(p)):
            s_occ[s[i]] = s_occ.get(s[i], 0) + 1
        

        lo, hi = 0, len(p) - 1
        
        while hi < len(s):
            anagram = True
            for key in p_occ:
                if p_occ[key] != s_occ.get(key, 0):
                    anagram = False
            for key in s_occ:
                if s_occ[key] != p_occ.get(key, 0):
                    anagram = False
            if anagram:
                res.append(lo)
                
            s_occ[s[lo]] -= 1
            lo += 1
            hi += 1
            if hi >= len(s):
                break
            s_occ[s[hi]] = s_occ.get(s[hi], 0) + 1
            
            
        return res
             
s = Solution
print(s.findAnagrams(None, "cbaebabacd","abc"))
# print(s.findAnagrams(None, "abab","ab"))