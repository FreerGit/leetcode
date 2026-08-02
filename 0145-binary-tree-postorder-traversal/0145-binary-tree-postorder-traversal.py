# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def dfs(a, t):

            if a:
                dfs(a.left, t)
                dfs(a.right, t)
                t.append(a.val)


        dfs(root, out)
        # print(out)
        return out