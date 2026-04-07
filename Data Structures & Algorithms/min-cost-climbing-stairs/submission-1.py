class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mini = [-1 for i in range(len(cost))]
        mini[0] = cost[0]
        mini[1] = cost[1]

        self.cost(len(cost)-1, cost, mini)

        return min(mini[-1], mini[-2])
    
    def cost(self, i, cost, mini):
        if mini[i] != -1:
            return mini[i]
        mini[i] = cost[i] + min(self.cost(i-1, cost, mini), self.cost(i-2, cost, mini))
        return mini[i]
