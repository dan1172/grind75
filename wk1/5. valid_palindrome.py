import re

def isPalindrome(self, s: str) -> bool:
    # s = re.sub("[^A-Za-z0-9]","",s.lower())
    s = [i for i in s.lower() if i.isalnum()]
    lo = 0
    hi = len(s) - 1
    while lo < len(s) - 1 and hi > 0:
        if s[lo] != s[hi]:
            return False
        lo = lo + 1
        hi = hi - 1
    return True