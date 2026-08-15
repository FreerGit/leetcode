class Solution:
    def hasSameDigits(self, s: str) -> bool:
        
        if len(s) > 2:
            t = ""
            for i in range(len(s) - 1):
                t += str((int(s[i]) + int(s[i +1])) % 10)

            return self.hasSameDigits(t)

        return s[0] == s[1]