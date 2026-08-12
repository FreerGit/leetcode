class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        cells = s.split(":")

        ma = 0
        mi = 10

        ma_alph = "A"
        mi_alph = "Z"

        for w in cells:
            a, n = w[0], int(w[1])

            ma = max(ma, n)
            mi = min(mi, n)
            ma_alph = max(ma_alph, a)
            mi_alph = min(mi_alph, a)

        ans = []
        for col in range(ord(mi_alph), ord(ma_alph) + 1):
            for row in range(mi, ma + 1):
                ans.append(chr(col) + str(row))

        return ans