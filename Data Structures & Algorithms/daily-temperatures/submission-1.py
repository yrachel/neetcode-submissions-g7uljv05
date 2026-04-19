class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for temp in temperatures]

        for i in range(len(temperatures)-1, -1, -1):
            for j in range(i - 1, -1, -1):
                if temperatures[i] > temperatures[j]:
                    if result[j] == 0:
                        result[j] = i - j
                    else:
                        result[j] = min(result[j], i - j)

        return result