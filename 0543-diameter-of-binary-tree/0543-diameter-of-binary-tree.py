# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_diameter=0

        def dfs(root):
            if root is None:
                return 0

            left_h=dfs(root.left)
            right_h=dfs(root.right)

            diameter=left_h+right_h
            self.longest_diameter=max(self.longest_diameter,diameter)
            return 1+ max(left_h,right_h)

        dfs(root)
        return self.longest_diameter
        
        