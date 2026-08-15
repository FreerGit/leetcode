class Solution:
    def countOppositeParity(self, nums):
        total_even = 0
        total_odd = 0

        # Count total evens and odds
        for num in nums:
            if num % 2 == 0:
                total_even += 1
            else:
                total_odd += 1

        even_seen = 0
        odd_seen = 0

        # Compute result in-place
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = total_odd - odd_seen
                even_seen += 1
            else:
                nums[i] = total_even - even_seen
                odd_seen += 1

        return nums