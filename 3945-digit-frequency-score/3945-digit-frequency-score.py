import collections

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        count = collections.defaultdict(int)

        for d in str(n):
            count[int(d)] += 1

        tot = 0
        for k,v in count.items():
            tot += k * v

        return tot