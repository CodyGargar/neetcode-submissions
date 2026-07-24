# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    max = 0
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return None
        
        self.recursion(root, root.val)
        
        return self.max
        

    def recursion(self, root, prevMax):
        if(not root):
            return
        
        if(root.val >= prevMax):
            self.max+=1
            prevMax = root.val

        self.recursion(root.right, prevMax)
        self.recursion(root.left, prevMax)