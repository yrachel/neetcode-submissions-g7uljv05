# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        attr = {}

        while stack:
            curr = stack[-1]
            if curr.left and curr.left not in attr:
                stack.append(curr.left)
            elif curr.right and curr.right not in attr:
                stack.append(curr.right)
            else:
                curr = stack.pop()
                print(curr.val)
                leftHeight, leftDiam = attr.get(curr.left, (0,0))
                rightHeight, rightDiam = attr.get(curr.right, (0,0))
                height = 1 + max(leftHeight, rightHeight)
                diameter = max(leftHeight + rightHeight, leftDiam, rightDiam)
                attr[curr] = (height, diameter)
        
        height, diameter = attr[root]
        return diameter
    
    