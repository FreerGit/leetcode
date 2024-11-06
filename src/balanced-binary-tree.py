class Solution:
    def traverse(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        l,r = self.traverse(root.left), self.traverse(root.right)

        if abs(l-r) > 1:
            self.valid = False
        
        return max(l,r) + 1
   
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        self.valid = True
        self.traverse(root)
        return self.valid
        