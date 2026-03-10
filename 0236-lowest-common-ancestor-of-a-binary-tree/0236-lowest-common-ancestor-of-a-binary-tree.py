# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # 1. edcase , root is not none
        if root is None:
            return None
        # 2. if current node is p, q , retunr it upward
        if root==p or root==q:
            return root
        # 3. search for p n q in theleft subtree
        left_result=self.lowestCommonAncestor(root.left,p,q)
        # 4. search for p and q in right subtree
        right_result=self.lowestCommonAncestor(root.right,p,q)
        # 5. If both sides ret a node , current node is LCA
        if left_result and right_result:
            return root
        # 6. Otherwise, return non null side, if exists
        return left_result if left_result else right_result

        