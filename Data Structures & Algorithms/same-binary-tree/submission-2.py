# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
            
        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            curr_p = p_stack.pop()
            curr_q = q_stack.pop()

            if curr_p.val != curr_q.val:
                return False
            
            if curr_p.left and curr_q.left:
                p_stack.append(curr_p.left)
                q_stack.append(curr_q.left)
            elif curr_p.left or curr_q.left:
                return False
            
            if curr_p.right and curr_q.right:
                p_stack.append(curr_p.right)
                q_stack.append(curr_q.right)
            elif curr_p.right or curr_q.right:
                return False

        if not p_stack and not q_stack:
            return True
        else:
            return False