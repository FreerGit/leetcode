class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)

        for n in nums:
            counter[n] += 1

        most_freq = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        output = []
        print(most_freq)
        for i in range(k):
            print(k)
            output.append(most_freq[i][0])

        return output