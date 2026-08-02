class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        out = len(words)

        for w in words:
            for c in w:
                if c not in allowed:
                    out -= 1
                    break
        
        return out