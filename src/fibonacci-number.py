class Solution:
    def helper(self, memo, n) -> int:
        if n == 0 or n == 1:
            return n
        if n not in memo:
            memo[n - 1] = self.helper(memo, n - 1)
            memo[n - 2] = self.helper(memo, n - 2)

        return memo[n -1] + memo[n - 2]
             

    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        return self.helper(memo, n)