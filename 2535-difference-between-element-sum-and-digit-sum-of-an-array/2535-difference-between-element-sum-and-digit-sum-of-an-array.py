class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        esum = 0
        dsum = 0

        for n in nums:
            esum += n
            while n > 0:
                dsum += (n % 10)
                n //= 10

        return abs(esum - dsum)