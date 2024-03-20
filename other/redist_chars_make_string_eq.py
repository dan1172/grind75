class Solution:
    def makeEqual(self, words) -> bool:
        occ = {}
        for w in words:
            for c in w:
                if c in occ:
                    occ[c] += 1
                else:
                    occ[c] = 1
        print(occ)
        return True
    
    
def makeEqual(words) -> bool:
    occ = {}
    n = len(words)
    if n <= 1:
        return True
    for w in words:
        for c in w:
            if c in occ: occ[c] += 1
            else: occ[c] = 1
    for i in occ.values():
        if i % n != 0: return False
    return True

# print(makeEqual(["ab","aabc","bc"]))
# print(makeEqual(["a","b"]))
# print(makeEqual(["abbab"]))
#print(makeEqual(["aa","aabaab"]))

print(makeEqual(["caaaaa","aaaaaaaaa","a","bbb","bbbbbbbbb","bbb","cc","cccccccccccc","ccccccc","ccccccc","cc","cccc","c","cccccccc","c"]))



# x = [1,1,1,1,1]
# x.remove(1)
# print(x)