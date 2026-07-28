class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals are sorted by start time 
        # to insert an interval, we have to check if they are overlapping
        # an overlapping interval has a start time that is <= to the previous interval's 
        # end. overlaps get merged 

        n = len(intervals)
        i = 0
        res = []

        # if the end of interval is less than start of new Interval, 
        # add the curr interval to final list
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # interval that overlaps with newInterval
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < n: 
            res.append(intervals[i])
            i += 1

        return res
        
            