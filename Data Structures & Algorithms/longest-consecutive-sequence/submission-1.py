class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        heapq.heapify(nums)
        longest = 0
        ongoing = 1
        prev = heapq.heappop(nums)

        while len(nums) > 0:
            curr = heapq.heappop(nums)
            
            if curr == prev + 1:
                ongoing += 1
            elif curr == prev:
                continue
            else:
                if ongoing > longest:
                    longest = ongoing
                ongoing = 1

            prev = curr

        if ongoing > longest:
            longest = ongoing
        return longest