class Solution:
    def clearDigits(self, s: str) -> str:
        n = 0
        while len(s) >= 2:
            if n >= 1 and s[n].isdigit():
                s = s[:n-1] + s[n+1:]
                n = 0
            
            n += 1

            if n >= len(s):
                break

        return s
