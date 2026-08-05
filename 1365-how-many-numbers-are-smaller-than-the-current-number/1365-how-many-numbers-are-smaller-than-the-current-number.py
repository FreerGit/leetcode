class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            v = 0
            for j in range(len(nums)):
                if i != j and nums[i] > nums[j]:
                    v += 1

            ans.append(v)

        return ans