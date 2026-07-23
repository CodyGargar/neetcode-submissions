# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if(root.val == p.val):
            return root

        if(root.val == q.val):
            return root

        if(not root):
            return None

        ancestorFound = True
        ans = root.val

        while(ancestorFound):
            ans = root.val  
            if(self.checkPresence(root.right, p, q)):
                root = root.right
            elif(self.checkPresence(root.left, p, q)):
                root = root.left
            else:
                return root


    def checkPresence(self, root, p, q):
        p_pres = False
        q_pres = False
        if(not root):
            return False
        qiu = deque([root])
        while(qiu):
            temp = qiu.pop()
            if temp == None:
                continue
            
            if(not p_pres and temp.val == p.val):
                p_pres = True
            if(not q_pres and temp.val == q.val):
                q_pres = True

            qiu.append(temp.left)
            qiu.append(temp.right)

            if(p_pres and q_pres):
                return True

        return False
            
            