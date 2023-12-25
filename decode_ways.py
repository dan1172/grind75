def isValid(s: str) -> bool: 
    if s[0] == '0':
        return False
    return 1 <= int(s) <= 26



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


def numDecodings(s: str) -> int:
    if s[0] == '0': return 0

    if isValid(s[:2]): n = 2 
    else: n = 1
    
    n1 = 1

    n, n1, n2 = 0, 0, 0
    for i in range(2, len(s)):
        n = 0
        print(f"string = {s[:(i + 1)]}")
        print(f"1 before = {s[:(i)]} and the one is {s[i:i+1]}")
        print(f"2 before = {s[:(i - 1)]} and the one is {s[(i-1):(i+1)]}")
        print()
        
        if isValid(s[i:i+1]):
            n += n1
        if isValid(s[(i-1):(i+1)]):
            n += n2 
        n = n1
        n1 = n2
    return n

print(numDecodings("11"))

# def numDecodings(s: str) -> int:
#     n = len(s)
#     dp = [0] * (n + 1)
#     if s[0] == '0':
#         dp[0] = 0
#     else:
#         dp[0] = 1
#     for i in range(1, n + 1):
#         c = 0
#         for j in range(i):
#             print(f"{j} {i}: {s[:j]}, {s[j:i]}")
#             #print(f"j = {j}, i = {i}, left = {s[:j]}, right is {s[j:i]}")
#             if dp[j] > 0 and isValid(s[j:i]):
#                 #print(f"left = {s[:j]}, right is {s[j:i]}, adding {dp[j]}")
#                 print(f"dp[j] = {dp[j]},  c = {c}")
#                 c += dp[j]
#         dp[i] = c
#     print(dp)
#     return dp[n]
    
    
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