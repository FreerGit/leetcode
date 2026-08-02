class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        out = nums

        for d in reversed(nums):
            out.append(d)

        return nums