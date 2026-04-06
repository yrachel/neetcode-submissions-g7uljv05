class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = " ".join(char for char in s.lower() if char.isalnum())

        return clean_str == clean_str[::-1]