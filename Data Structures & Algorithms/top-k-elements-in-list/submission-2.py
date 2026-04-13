class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        count = [[] for i in range(len(nums) + 1)]

        for key, value in freq.items():
            count[value].append(key)

        result = []
        print(count)
        for i in range(len(count) - 1, -1, -1):
            result.extend(count[i])

            if len(result) >= k:
                return result[0:k]

        return result[0:k]