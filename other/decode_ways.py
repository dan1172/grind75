def isValid(s: str) -> bool: 
    if s[0] == '0':
        return False
    return 1 <= int(s) <= 26

def numDecodings(s: str) -> int:
    if s[0] == '0': return 0
    if len(s) == 1: return 1
    if len(s) == 2:
        c = 0
        if isValid(s[:2]): c +=1
        if isValid(s[0]) and isValid(s[1]): c += 1
        return c

    n1, n2 = 1, 1
    for i in range(2, len(s) + 1):
        n = 0
        if isValid(s[(i-1):i]):
            n += n1
        if isValid(s[(i-2):i]):
            n += n2 
        n2 = n1
        n1 = n
   
    return n

print(numDecodings("27"))
    
    
# want to try 
# i = 0
# |1 

# i = 1
# |11 1|1 

# i == 2
# |111 1|11 11|1


# i == 3
# |1110 1|110 11|10 111|0

#i == 4
# |11106 1|11106 11|106 111|06 11110|6





class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        if s[0] == '0':
            dp[0] = 0
        else:
            dp[0] = 1
        for i in range(1, n + 1):
            c = 0
            for j in range(i):
                if dp[j] > 0 and isValid(s[j:i]):
                    c += dp[j]
            dp[i] = c
        return dp[n]