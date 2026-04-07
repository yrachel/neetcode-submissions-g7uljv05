"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms = []
        heapq.heapify(rooms)
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        for interval in sorted_intervals:
            start = interval.start
            end = interval.end
            if len(rooms) == 0:
                heapq.heappush(rooms, end)
            else:
                smallest = rooms[0]
                
                if smallest > start:
                    heapq.heappush(rooms, end)
                else:
                    heapq.heapreplace(rooms, end)
        return len(rooms)