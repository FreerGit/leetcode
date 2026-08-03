class Solution:
    def reverseDegree(self, s: str) -> int:
        tot = 0
        for i in range(len(s)):
            tot += (i + 1) * (ord('z') - ord(s[i]) + 1)
        return tot
