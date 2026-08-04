class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return bin(goal ^ start).count('1')