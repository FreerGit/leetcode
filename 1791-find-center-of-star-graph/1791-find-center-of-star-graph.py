from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        c = Counter()
        for l in edges:
            c.update(l)

        return c.most_common(1)[0][0]