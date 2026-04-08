def compare_versions(version_a: str, version_b: str) -> int:
    # --- STEP 1: DECONSTRUCTION ---
    # Convert "1.10.2" into ["1", "10", "2"]
    segments_a = version_a.split(".")
    segments_b = version_b.split(".")
    
    # --- STEP 2: DETERMINING SCOPE ---
    # We need to loop for whichever version has more "segments"
    # Example: "1.2" (2 segments) vs "1.2.1" (3 segments)
    total_segments_to_check = max(len(segments_a), len(segments_b))
    
    # --- STEP 3: THE SEGMENT-BY-SEGMENT COMPARISON ---
    for i in range(total_segments_to_check):
        
        # A. Get the numeric value for Version A at this position
        if i < len(segments_a):
            # Convert string "10" to integer 10
            value_a = int(segments_a[i])
        else:
            # If Version A is shorter, treat the missing slot as 0
            value_a = 0
            
        # B. Get the numeric value for Version B at this position
        if i < len(segments_b):
            value_b = int(segments_b[i])
        else:
            value_b = 0
            
        # --- STEP 4: THE TIE-BREAKER LOGIC ---
        # As soon as one value is bigger, we have a winner.
        if value_a > value_b:
            return 1   # version_a is newer/greater
        
        if value_b > value_a:
            return -1  # version_b is newer/greater
            
        # If they are equal (e.g., both are "1"), the loop continues 
        # to the next segment (e.g., the "Minor" or "Patch" version).

    # --- STEP 5: FINAL RESULT ---
    # If the loop finishes and we never returned 1 or -1, 
    # it means every segment was identical.
    return 0

# --- READABLE TEST SUITE ---
print(f"Is 1.10 newer than 1.2? Result: {compare_versions('1.10', '1.2')}")   # Expected: 1
print(f"Is 1.2.0 newer than 1.2? Result: {compare_versions('1.2.0', '1.2')}") # Expected: 0
print(f"Is 2.0.1 older than 2.1? Result: {compare_versions('2.0.1', '2.1')}") # Expected: -1