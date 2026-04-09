class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n + 1):
            output.append(self.count(i))

        return output

    def count(self, n):
        count = 0

        while n != 0:
            n &= (n-1)
            count += 1
        return count