class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    m = max(m, (nums[i] -1) * (nums[j] -1))
        
        return m