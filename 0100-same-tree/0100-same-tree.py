# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(a, t) -> List[int]:
            if a:
                t.append(a.val)
                rec(a.left, t)
                rec(a.right, t)
            else:
                t.append(None)

        t1 = []
        t2 = []
        rec(p, t1)
        rec(q, t2)    

        return t1 == t2        