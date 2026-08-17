class Solution:
    def replaceDigits(self, s: str) -> str:
        ans = []

        for i in range(0, len(s), 2):
            print(ans)
            ans.append(s[i])
            if i + 1 < len(s):
                ans.append(chr(ord(s[i]) + int(s[i+1])))

        return ''.join(ans)