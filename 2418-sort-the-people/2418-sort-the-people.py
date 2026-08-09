class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        z = zip(heights, names)
        ans = []
        for h,n in sorted(z, key= lambda x: x[0], reverse=True):
            ans.append(n)

        return ans