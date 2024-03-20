class Solution:
    def insert(self, intervals, newInterval):
        n = len(intervals)
        
        # check whether it fits perfectly before
        if intervals[0][0] > newInterval[1]:
            return newInterval + intervals
        
        # check if itt fits perfectly after
        if intervals[n - 1][1] < newInterval[0]:
            return intervals + newInterval
        
        # otherwise find first interval it overlaps with
        for i in range(len(intervals)):
            
        res = []
        # for i in intervals:
            



        return intervals


# check if it fits perfectly at the end or the start
    # if so, just chuck it at end or start
# otherwise, find first interval it overlaps with, and keep going 

# intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].