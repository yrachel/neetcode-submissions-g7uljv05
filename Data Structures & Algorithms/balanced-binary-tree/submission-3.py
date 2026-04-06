# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        balanced = True
        def height(root):
            nonlocal balanced
            if root is None:
                return 0
            left = height(root.left)
            right = height(root.right)

            if abs(left - right) > 1:
                balanced = False

            return 1 + max(left, right)

        left = height(root.left)
        right = height(root.right)
        return bool(abs(left - right) <= 1) and balanced
    
