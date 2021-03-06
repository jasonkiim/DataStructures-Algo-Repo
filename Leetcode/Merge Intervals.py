class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # start off by sorting the list by the start time
        r_type = []
        intervals = sorted(intervals, key = lambda x: x[0])

        # Appending to r_type and the last element in the r_type becomes the "previous" interval,
        # which should be appended if the r_type list is empty or the
        # start time of the current window does not overlap wit the last element.
        # If the end time of the "previous" time overlaps with the start time of the "current", then we want to find the new end time from current and prev. save as the
        # one that has the greater end time.
        for i in range(len(intervals)):
            if not r_type or r_type[-1][1] < intervals[i][0]:
                r_type.append(intervals[i])
            else:
                # Otherwise, there is an overlap, so merge the current and the previous
                r_type[-1][1] = max(r_type[-1][1], intervals[i][1])

        return r_type
