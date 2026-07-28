class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 1st condition: the new interval goes before all intervals
        # the interval start is less than the curr interval end

        # 2nd condition: insert the interval in an overlapping case
        # new start is <= the curr end AND the new end >= curr start
        
        # 3rd conditon: new interval inserted at the end

        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: 
                newInterval = [
                    min(newInterval[0], intervals[i][0]), 
                    max(newInterval[1], intervals[i][1])
                ]

        res.append(newInterval)
        return res
    
        













        n = len(intervals)
        i = 0
        res = []

        # if the end of interval is less than start of new Interval, 
        # add the curr interval to final list
        # add intervals before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # interval that overlaps with newInterval
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)

    # add all remaining intervals after newInterval
        while i < n: 
            res.append(intervals[i])
            i += 1

        return res

            