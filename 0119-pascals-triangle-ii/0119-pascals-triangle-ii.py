class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1], [1,1]]
        if rowIndex < 2:
            return ans[rowIndex]

        for i in range(2, rowIndex + 1):
            a = [1]

            for j in range(i):
                a.append(sum(ans[i - 1][j:j + 2]))
            ans.append(a)

        return ans[-1]