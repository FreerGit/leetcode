from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        seen = defaultdict(int)
        for c in magazine:
            seen[c] += 1

        for c in ransomNote:
            seen[c] -= 1
            if seen[c] < 0:
                return False
        
        return True