class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        dsum = 0
        sqsum = 0

        while n > 0:
            dsum += (n % 10)
            sqsum += (n % 10) ** 2

            n //=10

        return sqsum - dsum >= 50