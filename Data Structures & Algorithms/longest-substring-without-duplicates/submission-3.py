class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        substr = ""
        longest = 0

        for i, c in enumerate(s):
            if c in seen:
                longest = max(longest, len(substr))
                j = 0
                print(c)
                print(substr)
                print(seen)
                while substr[j] != c:
                    del seen[substr[j]]
                    j += 1

                substr = s[seen[c] + 1:i]
            seen[c] = i
            substr += c
        longest = max(longest, len(substr))
        return longest