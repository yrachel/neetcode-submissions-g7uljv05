class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = len(numbers) - 1

        while first != second:
            sum = numbers[first] + numbers[second]
            if sum == target:
                return [first + 1, second + 1]
            elif sum > target:
                second -= 1
            else:
                first += 1

        return []