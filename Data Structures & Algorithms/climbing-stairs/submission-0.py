class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1 for i in range(n)]

        return self.dfs(0, n, cache)
    
    def dfs(self, i, stop, cache):
        if (i >= stop):
            return i == stop
        elif cache[i] != -1:
            return cache[i]
        else:
            cache[i] = self.dfs(i + 1, stop, cache) + self.dfs(i + 2, stop, cache)
            return cache[i]