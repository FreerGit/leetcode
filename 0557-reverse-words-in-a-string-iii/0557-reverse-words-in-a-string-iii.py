class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        ans = []

        for w in l:
            ans.append(w[::-1])

        return ' '.join(ans)