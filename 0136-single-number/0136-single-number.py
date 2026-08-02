

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()

        x = nums[0]
        # print(nums)
        for i in range(1, len(nums) -1):
            if nums[i-1] != nums[i] and nums[i+1] != nums[i]:
                x = nums[i]
                continue

            if nums[i] == x:
                x = nums[-1]

        # print(x)
        return x

            

