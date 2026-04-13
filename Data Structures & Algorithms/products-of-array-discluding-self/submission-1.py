class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0] for i in range(len(nums))]
        suffix = [nums[len(nums) - 1] for i in range(len(nums))]
        output = [1 for i in range(len(nums))]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        output[0] = suffix[1]
        output[len(nums) - 1] = prefix[len(nums) - 2]

        for i in range(1, len(nums) - 1):
            print(i)
            output[i] = prefix[i - 1] * suffix[i + 1]

        return output