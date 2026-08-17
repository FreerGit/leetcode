class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()

        ans = len(words)

        for w in words:
            for c in w:
                if c in brokenLetters:
                    ans -= 1
                    break

        return ans