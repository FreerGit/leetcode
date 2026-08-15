class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        hs = sorted(heights)

        for i in range(len(heights)):
            if hs[i] != heights[i]:
                ans += 1


        return ans