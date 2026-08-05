import collections

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        
        ans = collections.deque()
        for n in reversed(nums):
            while n > 0:
                ans.appendleft(n % 10)
                n //= 10

        return list(ans)