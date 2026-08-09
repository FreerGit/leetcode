class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0

        for i in range(1, len(nums)):
            if abs(sum(nums[0:i]) - sum(nums[i: len(nums)])) % 2 == 0:
                ans += 1

        return ans