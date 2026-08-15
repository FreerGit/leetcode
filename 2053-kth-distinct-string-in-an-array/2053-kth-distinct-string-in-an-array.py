class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counts = Counter(arr)
        distinct = [x for x in arr if counts[x] == 1]

        return distinct[k - 1] if k <= len(distinct) else ""