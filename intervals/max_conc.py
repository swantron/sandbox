def count_runners(intervals):
    # --- STEP 0: THE EXIT ---
    # If the list is empty, we don't need any machines.
    if not intervals:
        return 0

    # --- STEP 1: TRANSFORMING DATA ---
    # State of 'intervals' at start: [[1, 5], [2, 4]]
    # We want to break these 'solid blocks' into 'individual events'.
    events = []
    
    for start, end in intervals:
        # Every interval creates TWO entries in our log.
        # Format: (Time, Change)
        events.append((start, 1))   # Someone arrived (+1)
        events.append((end, -1))    # Someone left (-1)
        
    # State of 'events' now: [(1, 1), (5, -1), (2, 1), (4, -1)]
    # (Notice they are currently out of order)

    # --- STEP 2: SORTING THE TIMELINE ---
    # We sort so we can walk through time from start to finish.
    events.sort()
    
    # State of 'events' now: [(1, 1), (2, 1), (4, -1), (5, -1)]
    # (Now they are in chronological order)

    # --- STEP 3: THE SWEEP ---
    # We walk through the events and keep track of the "Water Level".
    peak = 0     # The highest 'current' ever reached
    current = 0  # How many builds are running at THIS exact moment
    
    for time, change in events:
        # Update the 'current' count based on the event (+1 or -1)
        current += change
        
        # If 'current' just hit a new record, save it to 'peak'
        if current > peak:
            peak = current
            
        # --- MENTAL TRACE (Example [[1, 5], [2, 4]]) ---
        # 1. Time 1: change is +1 -> current=1, peak=1
        # 2. Time 2: change is +1 -> current=2, peak=2
        # 3. Time 4: change is -1 -> current=1, peak=2
        # 4. Time 5: change is -1 -> current=0, peak=2
            
    return peak

# --- RUNNING THE TEST ---
test_data = [[1, 5], [2, 4]]
result = count_runners(test_data)
print(f"Max runners needed: {result}")

test_data = [[1, 5], [2, 4], [1, 10]]
result = count_runners(test_data)
print(f"Max runners needed: {result}")

test_data = []
result = count_runners(test_data)
print(f"Max runners needed: {result}")