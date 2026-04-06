class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answers = {}

        for i in range(0, len(nums)):
            difference = target - nums[i]

            if difference in answers:
                return [answers[difference], i]
            else:
                answers[nums[i]] = i
        return None