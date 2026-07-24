# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque([root])
        count = 0
        visited = set()
        
        while q:
            temp = q[-1]
            
            if temp.left and temp not in visited:
                visited.add(temp)
                q.append(temp.left)
            else:
                q.pop()
                count += 1
                if count == k:
                    return temp.val
                if temp.right:
                    q.append(temp.right)
        
        return 0