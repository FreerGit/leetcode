class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []

        for o in operations:
            if o == "+":
                ans.append(sum(ans[-2:]))
            elif o == "D":
                ans.append(ans[-1] * 2)
            elif o == "C":
                ans.pop()
            else:
                ans.append(int(o))

        return sum(ans)
            