def merge_intervals(intervals):
    if not intervals:
        return []

    # 1. THE EVENT LOG (0=Start, 1=End)
    events = []
    for s, e in intervals:
        events.append((s, 0))
        events.append((e, 1))
    
    events.sort()

    # 2. THE STATE TRACKER
    merged = []
    current_active = 0
    start_time = None 

    for time, event_type in events:
        # MOMENT A: The room was empty, someone just walked in.
        # Record the time!
        if current_active == 0 and event_type == 0:
            start_time = time
        
        # UPDATE: Change the count
        if event_type == 0:
            current_active += 1
        else:
            current_active -= 1
        
        # MOMENT B: The last person just walked out.
        # Room is now empty (0). Save the period!
        if current_active == 0:
            merged.append([start_time, time])
            start_time = None # Reset the "sticky note"
            
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