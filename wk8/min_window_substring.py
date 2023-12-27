class Solution:
    def minWindow(self, s: str, t: str) -> str:
        return ""
    
    
def minWindow(s: str, t: str) -> str:
        
    
    return ""


# dictionary of occurences of each char in T

# dictionary of occurences in our current window

# "s" : 3





# t = "AABC"
# d1 = { "A" : 2, "B" : 1, "C" : 1}   # occureences in the t
# d2 = { "A" : 1, "B" : 1}  # occurences in the window

# check like d1["A"] == d2["A"]
# counter = 2 <- num distinct chars that ar efully satisfied
# 


# "ADOBECODEBANC"







# we want to maintain two pointers lo and hi 
# for the current window we are lookign at

# also, maintain a count of what characftesr have been
# satisfied by the curr window

# let the next character after hi that is not 
# currently included in the window be called "next"

# if all occurences of "next" in the window are not satisfied,
# then move hi to hi + 1 because we need to make our window
# contain the charactesr

# if it is satisfied, we have two cases
# one, is that s[lo] = s[next] already, so we can trivially move hi to hi + 1
# and lo to lo + 1 becuase we would like to traverse the rest of the string

# second case, is where s[lo] != s[next]
# we need to check if s[lo] is relevent to the satisfication


"X|ADOBEC|ODEBANC"
"ABC"
