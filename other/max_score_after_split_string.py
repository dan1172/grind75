# class Solution:
#     def maxScore(self, s: str) -> int:
#         lnz, rno, max_score, cur_score = 0, 0, 0, 0
#         for c in s:
#             if c == '1':
#                 rno += 1
#         for i in range(len(s) - 1):
#             if s[i] == '0':
#                 lnz += 1
#             elif s[i] == '1':
#                 rno -= 1
#             cur_score = lnz + rno
#             max_score = max(max_score, cur_score)
#         return max_score
                
class Solution:
    def maxScore(self, s: str) -> int:
        max_score, cur_score = 0, 0
        for c in s:
            if c == '1':
                cur_score += 1
        for i in range(len(s) - 1):
            if s[i] == '0':
                cur_score += 1
            elif s[i] == '1':
                cur_score -= 1
            max_score = max(max_score, cur_score)
        return max_score
                