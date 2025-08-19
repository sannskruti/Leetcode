# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                return "null"

            left_serialised=dfs(node.left)
            right_serialised=dfs(node.right)
            return str(node.val)+ ","+left_serialised+","+right_serialised
        return dfs(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values=data.split(",")
        self.index=0
        def build():
            if values[self.index]=="null":
                self.index+=1
                return None

            node=TreeNode(int(values[self.index]))
            self.index+=1
            node.left=build()
            node.right=build()
            return node
        return build()
     
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))