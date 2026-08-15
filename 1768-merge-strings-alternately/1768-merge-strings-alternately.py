class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        which = len(word1) < len(word2)
        mi = min(len(word1), len(word2))

        s = []

        for i in range(mi):
            s.append(word1[i])
            s.append(word2[i])

        
        if which:
            s.append(word2[mi:])
        else:
            s.append(word1[mi:])

        return ''.join(s)