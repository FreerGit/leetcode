from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = defaultdict()
        for i,v in enumerate(nums):
            left = target-v
            if m.__contains__(v):
                return [i, m[v]]
            m[v] = i