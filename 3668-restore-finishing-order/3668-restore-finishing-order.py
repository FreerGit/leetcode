class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        out = []
        
        for x in order:
            if x in friends:
                out.append(x)

        return out