class Solution:
    def countDigits(self, num: int) -> int:
        t = num
        a = 0

        while num > 0:
            a += t % (num % 10) == 0
            num //= 10

        return a