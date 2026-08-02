class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        out = ""

        for s in words:
            v = 0
            for c in s:
                v += weights[ord(c) - ord('a')]
            
            out += chr(ord('z') - (v % 26))
        
        return out