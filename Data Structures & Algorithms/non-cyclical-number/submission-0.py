class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        return self.happy(n, seen)
        
    def happy(self, n, seen):
        if n in seen:
            return False
        elif n == 1:
            return True
        else:
            seen.add(n)
            sum = 0

            while n > 0:
                sum += ((n % 10) ** 2)
                n = n // 10
            
            return self.happy(sum, seen)
