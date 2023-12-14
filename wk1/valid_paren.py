def isValid(s: str) -> bool:
    stack = []
    for c in s:
        if c == '[': 
            stack.append(']')
        elif c == '(': 
            stack.append(')')
        elif c == '{': 
            stack.append('}')
        elif len(stack) == 0:
            return False
        elif c != stack.pop():
            return False
    if len(stack) == 0: return True
    return False