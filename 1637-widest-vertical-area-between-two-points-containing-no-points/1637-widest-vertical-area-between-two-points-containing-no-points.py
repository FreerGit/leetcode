class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        ans = []

        for x,y in points:
            ans.append(x)

        ans.sort()

        m = 0
        for i in range(1, len(ans)):
            m = max(abs(ans[i -1] - ans[i]), m)

        return m
