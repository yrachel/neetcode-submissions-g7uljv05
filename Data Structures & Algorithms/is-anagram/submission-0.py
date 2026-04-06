class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ordered_s = sorted(s)
        if sorted(t) == ordered_s:
            return True
        return False