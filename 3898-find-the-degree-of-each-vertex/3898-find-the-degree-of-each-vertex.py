class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        out = []
        for i in range(len(matrix)):
            s = 0
            for j in range(len(matrix[i])):
                s += matrix[j][i]

            out.append(s)

        return out