class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        ans = []
        while n > 0:
            if s[n - 1] == '#':
                print(s[n-3:n-1])
                ans.append(chr(96 + int(s[n-3:n-1])))
                n -= 3
            else:
                ans.append(chr(96 + int(s[n-1])))
                n -= 1

        return ''.join(reversed(ans))
