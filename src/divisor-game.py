class Solution:
    def divisorGame(self, n: int) -> bool:
        def helper(n, alice_wins):
            alice_wins = not alice_wins
            if n == 1:
                return alice_wins
            
            return helper(n - 1, alice_wins)

        return helper(n, True)