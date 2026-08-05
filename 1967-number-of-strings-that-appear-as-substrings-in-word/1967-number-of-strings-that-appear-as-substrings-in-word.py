class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        a= 0
        for p in patterns:
            if word.find(p) != -1:
                a += 1
        return a