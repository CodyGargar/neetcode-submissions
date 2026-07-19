# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.invert(root) if root else None

    def invert(self, root):
        if(root.right or root.left):
            temp = root.right
            root.right = root.left
            root.left = temp

            self.invert(root.right) if root.right else None
            self.invert(root.left) if root.left else None

        return root