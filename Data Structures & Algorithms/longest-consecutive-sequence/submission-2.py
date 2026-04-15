class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = defaultdict(int)
        result = 0

        for num in nums:
            if not lengths[num]:
                lengths[num] = lengths.get(num - 1, 0) + 1 + lengths.get(num + 1, 0)
                lengths[num - lengths[num - 1]] = lengths[num]
                lengths[num + lengths[num+1]] = lengths[num]
                
                result = max(lengths[num], result)
        return result