import math
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        ma, mi = 0, 10000

        for n in nums:
            ma = max(n, ma)
            mi = min(n, mi)

        return math.gcd(ma,mi)