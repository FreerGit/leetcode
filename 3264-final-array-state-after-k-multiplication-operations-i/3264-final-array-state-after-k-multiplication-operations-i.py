class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            mi = min(nums)
            mi = nums.index(mi)
            nums[mi] = nums[mi] * multiplier

        return nums 