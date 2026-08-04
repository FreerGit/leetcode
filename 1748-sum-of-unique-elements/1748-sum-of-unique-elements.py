from collections import defaultdict
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        return sum(n for n, c in cnt.items() if c == 1)