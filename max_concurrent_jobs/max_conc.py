from typing import List

class Solution:
    def runners(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0  # Return 0, not []
        
        starts = sorted([i[0] for i in intervals])
        ends = sorted([i[1] for i in intervals])
        
        current_runners = 0
        max_runners = 0
        pointer_start = 0
        pointer_end = 0

        while pointer_start < len(starts):
            if starts[pointer_start] < ends[pointer_end]:
                current_runners += 1
                max_runners = max(max_runners, current_runners) # Peak check!
                pointer_start += 1
            else:
                current_runners -= 1
                pointer_end += 1

        return max_runners

sol = Solution()
print(f"Test 1 (Overlapping): {sol.runners([[1, 3], [2, 6]])}") # Should print 2
print(f"Test 2 (No overlap): {sol.runners([[1, 2], [4, 5]])}") # Should print 1
print(f"Test 3 (Empty): {sol.runners([])}") # Should print 0
print(f"Test 4 (Single): {sol.runners([[1, 2]])}") # Should print 1
