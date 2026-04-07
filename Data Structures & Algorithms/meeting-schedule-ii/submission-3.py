"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        curr = 0
        rooms = 0
        i = j = 0

        while i < len(start):
            if start[i] < end[j]:
                curr += 1
                rooms = max(curr, rooms)
                i += 1
            else:
                curr -= 1
                j += 1


        return rooms