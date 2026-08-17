class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        t = str(num)
        return str(int(t[::-1]))[::-1] == t 