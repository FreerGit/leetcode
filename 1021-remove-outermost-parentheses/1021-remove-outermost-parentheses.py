from collections import deque

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        x = 0
        ans = []
        for p in s:
            print(x)
            if p == '(':
                if x != 0:
                    ans.append(p)
                x += 1
            else:
                if x != 1:
                    ans.append(p)
                x -= 1

        return ''.join(ans)
