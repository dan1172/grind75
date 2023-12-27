class Solution:
    def minCost(self, colors: str, neededTime) -> int:
        n = len(neededTime)
        dp = [-1] * n
        
        # Base cases
        dp[0] = 0
        if colors[0] == colors[1]:
            dp[1] = min(neededTime[0], neededTime[1])
        else:
            dp[1] = 0
        
        # Recurrence
        for i in range(2, n):
            if colors[i] != colors[i-1]:
                dp[i] = dp[i - 2] # is this always the best option? # i think so
            else:
                dp[i] = dp[i - 2] + neededTime[i - 1]
        return min(dp[n - 1], dp[n-2] + neededTime[n-1])

# We are faced with a lot of decisions at each elemnt in the array, 
# so we can employ dynamic programming here

# Let dp[i] denote the least amount time required to make 
# the rope up to the original i'th baloon colourful, including the i'th balloon

# note that we dont necessariyl need to include the last baloon as well,
# so we will have n + 1 number of subproblems

# recurreucne is as follows
# we if color[i] == colour[i-1], then dp[i] = dp[i-2] + neededTime[i-1]
# if color[i] != colour[i-1], then dp[i] = dp[i-1]



# def minCost(colors: str, neededTime) -> int:
#     n = len(neededTime)
#     if n == 1:
#         return 0
    
#     dp = [-1] * n
    
#     # Base cases
#     dp[0] = 0
#     if colors[0] == colors[1]:
#         dp[1] = min(neededTime[0], neededTime[1])
#     else:
#         dp[1] = 0
    
#     # Recurrence
#     for i in range(2, n):
#         if colors[i] != colors[i-1]:
#             dp[i] = dp[i - 1] # is this always the best option? # i think so
#         else:
#             back = i - 1
#             time_used = 0
#             while back >= 0:
#                 if colors[back] != colors[i]:
#                     break
#                 time_used += neededTime[back]
#                 back -= 1
#             # go back until you find a diff colour and take away all the needed
#             if back < 0: 
#                 dp[i] = time_used
#             else:
#                 dp[i] = dp[back] + time_used
#     print(dp)
#     return min(dp[n - 1], dp[n-2] + neededTime[n-1])

#print(minCost("aaaa", [8,7,2,10]))
#print(minCost("aabaa", [1,2,3,4,1]))
#print(minCost("baab", [8,7,2,10]))


def minCost(colors: str, neededTime):
    
    return 0 