class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        g = g[::-1]
        s.sort()
        s = s[::-1]
        counter = 0
        for gp, sp in zip(g, s):
            if sp >= gp:
                counter += 1
            else:
                break
        return counter
                
                
def findContentChildren(g, s) -> int:
    g.sort()
    s.sort()
    counter = 0
    i, j = 0, 0
    while i < len(g) and j <len(s):
        if s[j] >= g[i]:
            counter += 1
            j += 1
            i += 1
        else:
            j += 1
    return counter
           
#print(findContentChildren([1,2,3],[1,1])) # expect 1
# print(findContentChildren([1,2],[1,2,3]))  # expect 2
print(findContentChildren([10,9,8,7],[5,6,7,8])) # expected = 2