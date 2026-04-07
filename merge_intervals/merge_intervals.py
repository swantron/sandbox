from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start time
        # pull first value (index 0) from interval
        # sort
        # handle single intervals and empty intervals
        
        #empty
        if not intervals:
            return []
        
        # sort 'em
        intervals.sort()

        # init merged intervals
        merged = []
        # main logic
        for current in intervals:
            # check for empty merge or no overlap
            # compare end time of last processed item
            # to begin of current item
            if not merged or merged[-1][1] < current[0]: #? check logic
                merged.append(current)
            else:
                # overlap found
                merged[-1][1] = max(merged[-1][1], current[1])

        return merged

