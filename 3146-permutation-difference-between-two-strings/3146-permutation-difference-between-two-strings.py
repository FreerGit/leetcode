class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        tot = 0

        for i in range(len(s)):
            tot += abs(i - t.index(s[i]))

        return tot