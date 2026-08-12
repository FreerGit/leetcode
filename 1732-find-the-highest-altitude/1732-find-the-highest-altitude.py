class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        tt = 0

        m = 0

        for g in gain:
            tt += g
            m = max(m, tt)

        return m