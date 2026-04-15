class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen = set([nums[0]])
        results = set()
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                option = (nums[i], nums[j], target)
                if target in seen:
                    results.add((nums[i], nums[j], target))
            
            seen.add(nums[i])

        return [[first, second, third] for first, second, third in results]