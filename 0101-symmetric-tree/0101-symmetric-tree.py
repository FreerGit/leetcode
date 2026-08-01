# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        a = []
        b = []

        def dfs_left(x, t) -> List[int]:
            if x:
                t.append(x.val)
                dfs_left(x.left, t)
                dfs_left(x.right, t)
            else:
                t.append(None)


            return t

        def dfs_right(x, t) -> List[int]:
            if x:
                t.append(x.val)
                dfs_right(x.right, t)
                dfs_right(x.left, t)
            else:
                t.append(None)
            return t

        dfs_left(root, a)
        dfs_right(root, b)

        return a == b