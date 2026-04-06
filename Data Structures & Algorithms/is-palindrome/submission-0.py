class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = s.lower()
        i = 0
        j = len(s) - 1

        while i < j:
            if not clean_str[i].isalnum():
                i += 1
            elif not clean_str[j].isalnum():
                j -= 1
            elif clean_str[i] != clean_str[j]:
                return False
            else:
                i += 1
                j -= 1
        return True