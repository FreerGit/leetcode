class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        tot = 0

        for i in range(len(nums)):
            if i % 2 == 0:
                tot += nums[i]
            else:
                tot -= nums[i]

        return tot