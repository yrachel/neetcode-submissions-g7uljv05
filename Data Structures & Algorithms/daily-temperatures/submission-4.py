class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for temp in temperatures]
        
        for i in range(len(temperatures)-2, -1, -1):
            j = i + 1

            while j < len(temperatures) - 1 and temperatures[j] <= temperatures[i]:
                if result[j] == 0:
                    break
                else:
                    j += result[j]

            if temperatures[j] > temperatures[i]:
                result[i] = j - i

        return result