class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        out = 0

        for i in nums:
            out += min(abs(3 - ( i % 3)), abs(0 - (i % 3)))


        return out