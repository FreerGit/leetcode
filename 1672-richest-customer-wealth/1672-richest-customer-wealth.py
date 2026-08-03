class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = 0

        for a in accounts:
            v = 0
            for i in a:
                v += i

            m = max(m, v)
        
        return m