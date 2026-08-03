class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftSum = [0] * len(nums)
        rightSum = [0] * len(nums)
        print(leftSum, rightSum)

        for i in range(len(nums)):
            leftSum[i] = sum(nums[:i])
            rightSum[i] = sum(nums[i+1:])

        out = []
        for i in range(len(leftSum)):
            out.append(abs(leftSum[i] - rightSum[i]))

        return out