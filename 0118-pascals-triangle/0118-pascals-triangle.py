class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        a = [[] for i in range(numRows)]
        # print(a)
        for i in range(numRows):
            a[i].append(1)
            if i == 0:
                continue
            
            if i >= 2:
                for y in range(len(a[i-1]) - 1):
                    # print(a[i-1][y:y+1])
                    a[i].append(sum(a[i-1][y:y+2]))

            a[i].append(1)

        return a
