def merge_intervals(intervals):
    if not intervals:
        return []

    # 1. THE EVENT LOG
    events = []
    for start, end in intervals:
        events.append((start, 1))   # Build Starts
        events.append((end, -1))    # Build Ends

    # 2. THE SORT (with tie-breaker)
    # We use -x[1] so that if times are the same, 
    # the Start (+1) is processed before the End (-1).
    events.sort(key=lambda x: (x[0], -x[1]))

    # 3. THE MERGE SWEEP
    merged = []
    current_active = 0
    start_time = None 

    for time, change in events:
        # If we are at 0 and see a start, this is the birth of a new block
        if current_active == 0:
            start_time = time
        
        current_active += change
        
        # If we drop back to 0, the block is "closed"
        if current_active == 0:
            merged.append([start_time, time])
            
    return merged

# --- TEST CHECKS ---

# Test 1: Standard Overlap
# [1,3] and [2,6] should merge into [1,6]
print(f"Test 1 (Overlap): {merge_intervals([[1, 3], [2, 6], [8, 10]])}")
# Expected: [[1, 6], [8, 10]]

# Test 2: Touching Endpoints
# One ends at 4, next starts at 4. They should merge.
print(f"Test 2 (Touching): {merge_intervals([[1, 4], [4, 5]])}")
# Expected: [[1, 5]]

# Test 3: Completely Contained
# [2, 5] is entirely inside [1, 10]
print(f"Test 3 (Contained): {merge_intervals([[1, 10], [2, 5]])}")
# Expected: [[1, 10]]

# Test 4: Unsorted Input
print(f"Test 4 (Unsorted): {merge_intervals([[15, 18], [1, 3]])}")
# Expected: [[1, 3], [15, 18]]