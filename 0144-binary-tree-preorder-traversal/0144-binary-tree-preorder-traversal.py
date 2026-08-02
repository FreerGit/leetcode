# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        out = []

        def dfs(a, t):

            if a:
                t.append(a.val)
                dfs(a.left, t)
                dfs(a.right, t)


        dfs(root, out)
        # print(out)
        return out