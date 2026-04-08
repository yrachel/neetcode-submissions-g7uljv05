class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
            
        slow = n
        fast = self.sumOfSquares(n)

        while slow != fast:
            if slow == 1 or fast == 1:
                return True
            else:
                slow = self.sumOfSquares(slow)
                fast = self.sumOfSquares(self.sumOfSquares(fast))

        return False
        
    def sumOfSquares(self, n):
        sum = 0

        while n > 0:
            sum += ((n % 10) ** 2)
            n = n // 10
        
        return sum
