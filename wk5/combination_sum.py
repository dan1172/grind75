class Solution:
    def combinationSum(self, candidates, target: int):
        dp = [] * (target + 1)
        return None
    
def combinationSum(candidates, target: int):
    dp = [None for _ in range((target + 1))]
    smallest = min(candidates)
    dp[smallest] = [[smallest]]
    candidates.sort()
    for i in range(smallest + 1, target + 1):
        for j in candidates:
            if j > i: 
                break
            if (dp[i - j]) != None:
                if dp[i] == None:
                    dp[i] = []
                for combo in dp[i - j]:
                    new = combo.copy()
                    new.append(j)
                    dp[i].append(new)
            if j == i:
                if dp[i] == None:
                    dp[i] = []
                dp[i].append([j])

            
    for i in range(len(dp)):
        print(f"dp[{i}] = {dp[i]}")
        #res.add(tuple(dp))
    for c in dp[target]:
        c.sort()
    res = set(tuple(i) for i in dp[target])
    #return dp[target]
    return res

print(combinationSum([1, 2], 3))
        
# subproblem: dp[i] is how many disticnt combinations 
# of numbers to sum to exactly i

# base
# dp[min(candiates)] = [min(candidates)]
# dp[i (for i < min(candiates)] = []

# recurrence
# dp[i] = for all j in candidates
# if dp[i - j] != [], then dp[i].append(dp[i-j].append(j))
