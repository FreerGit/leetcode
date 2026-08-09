class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        out = []

        for i in range(0, len(nums)  - 1 , 2):
            out.append(nums[i + 1])
            out.append(nums[i])
        
        return out