# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):

            v = 0
            if root:
                if low <= root.val <= high:
                    v = root.val

                return v + dfs(root.left) + dfs(root.right)
            return v                

        return dfs(root)