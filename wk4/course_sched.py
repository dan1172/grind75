class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        if len(prerequisites) == 0:
            return True
        
        first = prerequisites[0][0]
        
        # so this here is clearly a cycle detection algorithm
        prev = [-1 for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        
        # run a dfs to look for cycles
        stack = []
        
        while stack:
            e = stack.pop()
            if (visited[e]):
                continue
            visited[e] = True
            for p in [p for p in prerequisites if p[0] == e]:
                if prev[p[1]] != -1:
                    return False
                prev[p[1]] = e
                stack.append(p[1])
                
        
        return True
    
# s = Solution()
# p = 