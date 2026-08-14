class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        mi = 1000000
        for s,t in tasks:
            mi = min(mi, s + t)

        return mi