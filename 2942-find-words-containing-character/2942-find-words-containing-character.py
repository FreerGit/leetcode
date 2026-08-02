class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        out = []

        for w in range(len(words)):
            if x in words[w]:
                out.append(w)

        return out