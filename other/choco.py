class Solution:
    def buyChoco(self, prices, money) -> int:
        c1 = 101
        c2 = 101
        for p in prices:
            l = [c1, c2, p]
            l.remove(max(l))
            c1 = l[0]
            c2 = l[1]
        if money - (c1 + c2) >= 0:
            return money - (c1 + c2)
        else:
            return money
        
        
