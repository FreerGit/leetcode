class Solution:
    def countAsterisks(self, s: str) -> int:
        t = 0
        ans =0
        for c in s:
            if t == 0 and c == '*':
                ans += 1

            if c == '|':
                if t == 0:
                    t += 1
                else:
                    t -= 1
        return ans
