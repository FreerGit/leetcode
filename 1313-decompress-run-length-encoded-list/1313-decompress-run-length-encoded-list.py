class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(int(len(nums) / 2)):
            ans.extend(nums[i * 2] * [nums[i * 2 + 1]])

        return ans