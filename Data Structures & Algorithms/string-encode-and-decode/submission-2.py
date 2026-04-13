class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result = result + str(len(s)) + "&" + s

        return result

    def decode(self, s: str) -> List[str]:
        i = 0
        length = ""
        result = []

        while i < len(s):
            if s[i] == "&":
                length = int(length)
                curr = s[i+1:i+length+1]
                result.append(curr)
                i = i + length + 1
                length = ""
            else:
                length += s[i]
                i += 1

        return result