# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.p = None

        def dfs(root, t):

            if root:
                if root.val == t:
                    self.p = root

                dfs(root.right, t)
                dfs(root.left, t)

        dfs(cloned, target.val)
        return self.p 

