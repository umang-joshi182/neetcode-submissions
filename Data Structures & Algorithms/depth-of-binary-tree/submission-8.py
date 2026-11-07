# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            stack = []
            right = 1
            if node.right:
                right += 1
            if node.left:
                right += 1
            
            dfs(node.left)
            dfs(node.right)
            stack.append(right)
            return max(stack)
        return dfs(root)
        