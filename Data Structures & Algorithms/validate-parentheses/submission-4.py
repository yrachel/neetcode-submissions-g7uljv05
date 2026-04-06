class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closing = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        
        for char in s:
            if char not in closing:
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()
                if prev != closing[char]:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False