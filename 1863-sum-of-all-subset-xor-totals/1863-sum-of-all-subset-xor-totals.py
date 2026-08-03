import itertools
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        tot = 0
        for r in range(len(nums) + 1):
            for subset in combinations(nums, r):
                tot += reduce(xor, subset, 0)
        return tot