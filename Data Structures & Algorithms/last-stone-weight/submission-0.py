class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones = sorted(stones)
            x = stones.pop()
            y = stones.pop()
            diff = x - y

            if diff > 0:
                stones.append(diff)

        return stones[0] if len(stones) == 1 else 0