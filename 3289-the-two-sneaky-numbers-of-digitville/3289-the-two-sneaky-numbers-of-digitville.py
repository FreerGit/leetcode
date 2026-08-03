class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        out = []
        for i in nums: 
            if i in seen:
                out.append(i)
            seen.add(i)
            

        return out