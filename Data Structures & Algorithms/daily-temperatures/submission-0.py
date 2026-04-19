class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for temp in temperatures]

        for i in range(len(temperatures)):
            for j in range(i - 1, -1, -1):
                if result[j] == 0 and temperatures[i] > temperatures[j]:
                    result[j] = i - j

        return result