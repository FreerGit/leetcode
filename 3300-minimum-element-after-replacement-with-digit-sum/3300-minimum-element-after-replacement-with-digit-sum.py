class Solution:
    def minElement(self, nums: List[int]) -> int:
        out = []

        for i in nums:
            x = i
            s = 0
            while i > 0:
                s += i % 10
                i //= 10
            out.append(s)

        out.sort()

        return out[0]

            