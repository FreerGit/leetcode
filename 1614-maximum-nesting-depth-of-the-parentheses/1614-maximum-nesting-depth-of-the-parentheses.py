class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        m = 0
        for c in s:
            if c == '(':
                ans += 1
            elif c == ')':
                ans -= 1

            m = max(m, ans)
        return m