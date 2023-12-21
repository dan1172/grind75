class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ap = len(a)
        bp = len(b)
        res = ""
        carry = 0
        while ap >= 0 and bp >= 0:
            an = int(a[ap]) 
            bn = int(b [bp]) 
            total = an + bn + carry
            if total == 0:
                res.insert(0, '0')
            else: 
                res.insert(0, '0')
                carry = total - 1
            ap = ap - 1
            bp = bp - 1
        if ap < 0 and bp < 0:
            return res
        elif bp < 0:
            # continue prepending from a
            while (ap >= 0):
                total = int(a[ap]) + carry:
                    