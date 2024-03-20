
def addBinary(a: str, b: str) -> str:
    max_len = max(len(a), len(b))
    a, b = a.rjust(max_len, "0"),  b.rjust(max_len, "0")
    res = ""
    carry = 0
    i = max_len - 1
    while i > -1:
        an, bn = int(a[i]), int(b[i])
        carry += (an + bn)
        if carry == 0:
            res = res + '0'
        elif carry == 1:
            res = res + '1'
            carry = 0
        elif carry == 2:
            res = res + '0'
            carry = 1
        elif carry == 3:
            res = res + '1'
            carry = 1
        i -= 1
    res = res + '1' * carry
    return res[::-1]

print(addBinary("1010", "1011"))
# "11" + "11" = "0110"