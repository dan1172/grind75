class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (s == ""): return 0

        dp = [0] * len(s)
        for i in range(len(s)):
            if i == 0:
                dp[i] = 1
            else:
                # traverse backwards until you find that character again or you go out of bounds
                counter = 1
                chars = set()
                for j in range(i - 1, -1, -1):
                    print(s[j])
                    if s[j] == s[i] or s[j] in chars: break
                    else:
                        chars.add(s[j])
                        counter = counter + 1
                dp[i] = counter
        print(dp)
        return max(dp)
    
    
    # if it appears before 