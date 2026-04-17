class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0

        for i in range(len(s)):
            curr = s[i]
            edits, l, r = 0, i, i

            while edits <= k and r < len(s):
                if s[r] != curr:
                    if edits == k:
                        break
                    edits += 1
                r += 1

            while edits <= k and l > 0:
                if s[l - 1] != curr:
                    if edits == k:
                        break
                    edits += 1
                l -= 1

            longest = max(longest, r - l)

        return longest