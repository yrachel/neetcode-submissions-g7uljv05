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
            
        stack = [root]
        height = {}

        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in height:
                stack.append(curr.left)
            elif curr.right and curr.right not in height:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                left = height.get(curr.left, 0)
                right = height.get(curr.right, 0)

                if abs(left - right) > 1:
                    return False
                else:
                    height[curr] = 1 + max(left, right)

        return True
    
