class Solution:
    def insert(self, intervals, newInterval):
        # step 1: find last interval that has an earlier starting time than new
        last = intervals[0]
        for i in intervals:
            if intervals