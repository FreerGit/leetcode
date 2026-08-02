class Solution:
    def convertDateToBinary(self, date: str) -> str:
        o = date.split('-')

        out = []
        for x in o:
            out.append(bin(int(x))[2:])

        return '-'.join(out)