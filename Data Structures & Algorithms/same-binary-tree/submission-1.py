# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if(not p and not q):
            return True
        if((not p and q) or (not q and p)):
            return False

        q1 = deque()
        q1.append(p)
        
        q2 = deque()
        q2.append(q)

        while(q1 and q2):
            size = len(q1)
            
            for _ in range(size):
                temp1 = q1.pop()
                temp2 = q2.pop() 
                if(temp1 and temp2):
                    if(temp1.val != temp2.val):
                        print("False by comparision")
                        return False
                    else:
                        q1.append(temp1.left)
                        q1.append(temp1.right)
                        q2.append(temp2.left)
                        q2.append(temp2.right)
                elif(temp1 and not temp2) or (temp2 and not temp1):
                    return False

                
        if(len(q1) != len(q2)):
            return False
        return True
                
