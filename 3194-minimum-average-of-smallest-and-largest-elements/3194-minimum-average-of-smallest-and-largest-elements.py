class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        d = deque(nums)
        avgs = []
        for i in range(len(nums) // 2):
            avgs.append((d.popleft() + d.pop()) / 2)

        return min(avgs)