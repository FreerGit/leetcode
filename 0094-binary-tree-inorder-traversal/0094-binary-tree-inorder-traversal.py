# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        t = []
        def inOrder(root, t: List[int]) -> List[int]:

            if root == None:
                return

            inOrder(root.left, t)

            t.append(root.val)

            inOrder(root.right, t)

            return t

        inOrder(root, t)
        return t