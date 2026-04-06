class Solution:
    def search(self, nums: List[int], target: int) -> int:
        middle = len(nums)//2
        left = 0
        right = len(nums)

        while left <= right and middle < len(nums):
            print(middle)
            if nums[middle] == target:
                return middle

            if target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
            middle = (left + right) // 2
        return -1
