"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        timeline = defaultdict(int)
        curr = 0
        result = 0

        for interval in sorted_intervals:
            timeline[interval.start] += 1
            timeline[interval.end] -= 1
        for i in sorted(timeline.keys()):
            curr += timeline[i]
            result = max(curr, result)

        return result