class Solution:
    def sortSentence(self, s: str) -> str:
        ss = s.split()
        ans = [""] * len(ss)
        for i in ss:
            ans[int(i[-1]) - 1] = i[:len(i)-1]

        return ' '.join(ans)