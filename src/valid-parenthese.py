class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                open_p = stack.pop()
                if ((open_p == '(' and c != ')') or
                    (open_p == '[' and c != ']') or
                    (open_p == '{' and c != '}')):
                    return False
        
        return len(stack) == 0