class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            curr = target - numbers[i]

            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == curr:
                    return [i + 1, mid + 1]
                elif numbers[mid] > curr:
                    r -= 1
                else:
                    l += 1

        return []