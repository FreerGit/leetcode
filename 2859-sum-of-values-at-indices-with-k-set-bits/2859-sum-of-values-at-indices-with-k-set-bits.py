class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        a = 0

        for n in range(len(nums)):
            if bin(n).count('1') == k:
                a += nums[n]

        return a