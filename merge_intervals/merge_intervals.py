def merge_intervals(intervals):
    # --- STATE: input intervals = [[1, 4], [4, 5]] ---
    if not intervals:
        return []

    # 1. THE EVENT LOG
    events = []
    for start, end in intervals:
        events.append((start, 0)) # 0 = START
        events.append((end, 1))   # 1 = END
    
    # --- STATE: events (unsorted) = [(1, 0), (4, 1), (4, 0), (5, 1)] ---

    # 2. THE SORT
    # Because (4, 0) is "smaller" than (4, 1), the START happens first.
    events.sort()

    # --- STATE: events (sorted) = [(1, 0), (4, 0), (4, 1), (5, 1)] ---

    # 3. THE MERGE SWEEP
    merged = []
    current_active = 0
    start_time = None 

    for time, event_type in events:
        # --- STATE TRACE ---
        
        # EVENT 1: (1, 0)
        # current_active is 0, event_type is 0 (START)
        if current_active == 0 and event_type == 0:
            start_time = 1  # Bookmark the start!
        
        # Update count: 0 -> 1
        if event_type == 0:
            current_active += 1
        else:
            current_active -= 1
        
        # current_active is 1. We don't close the interval yet.

        # EVENT 2: (4, 0) (The second interval starts)
        # Update count: 1 -> 2
        # current_active is now 2. start_time is still 1.

        # EVENT 3: (4, 1) (The first interval ends)
        # Update count: 2 -> 1
        # current_active is now 1. It didn't hit 0, so the flashlight stays ON.

        # EVENT 4: (5, 1) (The final interval ends)
        # Update count: 1 -> 0
        if event_type == 1: # We don't actually need this 'if', it's just for the trace
             pass 

        # If the 'Flashlight' just turned off (current_active is 0)
        if current_active == 0:
            # Finalize the block!
            merged.append([start_time, time]) # merged = [[1, 5]]
            
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