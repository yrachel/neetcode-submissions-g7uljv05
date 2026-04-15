class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        seen = set([nums[0]])
        results = []
        duplicates = set()
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                option = (nums[i], nums[j], target)
                if target in seen and option not in duplicates:
                    results.append([nums[i], nums[j], target])
                    duplicates.add((nums[i], nums[j], target))
            
            seen.add(nums[i])

        return results