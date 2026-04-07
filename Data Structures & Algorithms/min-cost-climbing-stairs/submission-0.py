class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mini = [-1 for i in range(len(cost))]
        mini[0] = cost[0]
        mini[1] = cost[1]

        for i in range(2, len(mini)):
            mini[i] = cost[i] + min(mini[i-1], mini[i-2])
        
        return min(mini[-1], mini[-2])