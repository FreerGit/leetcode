class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []

        for i in range(len(prices)):
            disc = False
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    ans.append(prices[i] - prices[j])
                    disc = True
                    break
            if not disc:
                ans.append(prices[i])
            disc = False

        return ans