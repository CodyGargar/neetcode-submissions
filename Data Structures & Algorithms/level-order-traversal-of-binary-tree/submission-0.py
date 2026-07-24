# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if( not root):
            return ans
        q = deque([root])

        while q:
            size = len(q)
            templist = []
            for _ in range(size):
                temp = q.popleft()
                if temp:
                    templist.append(temp.val)
                    if(temp.left):
                        q.append(temp.left)
                    if(temp.right):
                        q.append(temp.right)
                
            ans.append(templist)

        return ans
