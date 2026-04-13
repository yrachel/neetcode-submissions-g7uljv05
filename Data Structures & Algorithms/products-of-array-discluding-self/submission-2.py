class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros = 0
        pos = -1
        everything = 1

        for index, num in enumerate(nums):
            if num == 0:
                zeros += 1
                pos = index
            else:
                everything *= num

        if zeros >= 2:
            result = [0 for i in range(len(nums))]
        elif zeros == 1:
            result = [0 for i in range(len(nums))]
            result[pos] = everything
        else:
            result = [everything // num for num in nums]
        
        return result