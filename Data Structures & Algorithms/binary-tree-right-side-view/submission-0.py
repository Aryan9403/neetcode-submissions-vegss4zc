# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        ans = []
        
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            ans.append(level[0])
            
        return ans