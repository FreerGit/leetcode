class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            i = word.index(ch)
        except:
            return word

        return word[:i + 1][::-1] + word[i+ 1:]