class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        acr = ""

        for w in words:
            acr += w[0]

        return acr == s