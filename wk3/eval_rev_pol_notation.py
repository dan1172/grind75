class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*']:
                n1 = stack.pop()
                n2 = stack.pop()
                new = eval(f"{n2}{t}{n1}")
                stack.append(new)
            elif t == '/':
                n1 = stack.pop()
                n2 = stack.pop()
                new = int(n2 / n1)
                stack.append(new)
            else:
                stack.append(int(t))
        return stack.pop()
    
s = Solution()
tokens = ["4","13","5","/","+"]
print(s.evalRPN(tokens))