class Solution:
    def balancedStringSplit(self, s: str) -> int:
        b = 0
        ans = 0
        for c in s:
            if c == 'R':
                b -= 1
            elif c == 'L':
                b += 1

            if b == 0:
                ans += 1

        return ans