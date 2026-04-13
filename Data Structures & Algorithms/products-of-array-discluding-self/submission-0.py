class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            if i == 0:
                output[i] = math.prod(nums[i+1:])
            elif i == len(nums) - 1:
                output[i] = math.prod(nums[0:i])
            else:
                output[i] = math.prod(nums[0:i]) * math.prod(nums[i+1:])

        return output