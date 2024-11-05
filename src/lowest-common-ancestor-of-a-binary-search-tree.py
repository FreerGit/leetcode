class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(curr, r):
            if not r:
                return curr

            curr = r
            if r.val == p.val or r.val ==  q.val:
                return curr
            if r.val > p.val and r.val > q.val:
                return dfs(curr, r.left)
            if r.val < p.val and r.val < q.val:
                return dfs(curr, r.right)
    
            return curr

        res = dfs(root, root)
        return res