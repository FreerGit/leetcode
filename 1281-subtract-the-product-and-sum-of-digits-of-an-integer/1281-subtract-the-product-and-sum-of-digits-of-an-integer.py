class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        s = 0
        
        while n > 0:
            x = n % 10
            n //= 10
            prod *= x
            s += x

        return prod - s