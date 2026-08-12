class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0

        for w in words:
            ans += w.startswith(pref)

        return ans