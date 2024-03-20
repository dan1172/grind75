class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return 0
    
    
# def maxLengthBetweenEqualCharacters(self, s: str) -> int:
#     d = {}
#     length = -1
#     for i in range(len(s)):
#         if s[i] in d:
#             length = max(length, i - d[s[i]] - 1)
#         else:
#             d[s[i]] = i
#     return length


def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    d = [-1] * 27
    length = -1
    for i in range(len(s)):
        if s[i] in d:
            length = max(length, i - d[s[i]] - 1)
        else:
            d[s[i]] = i
    return length


print(maxLengthBetweenEqualCharacters(None, "abca"))