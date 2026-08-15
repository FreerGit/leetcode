class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        kv = defaultdict(int)

        for k,v in nums1:
            kv[k] += v

        for k,v in nums2:
            kv[k] += v

        ans = []

        for k,v in sorted(kv.items()):
            ans.append([k,v])

        return ans
