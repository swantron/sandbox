def compare_versions(v1: str, v2: str) -> int:
    # 1. THE SPLIT
    # Convert "1.2.1" -> ["1", "2", "1"]
    list1 = v1.split(".")
    list2 = v2.split(".")
    
    # 2. THE LENGTH CHECK
    # We need to know how many "slots" to check (Major, Minor, Patch, etc.)
    max_length = max(len(list1), len(list2))
    
    # 3. THE LOOP
    for i in range(max_length):
        # Grab the number at this slot. 
        # If the list ran out of numbers, use 0.
        
        # Part A: Get value for v1
        if i < len(list1):
            n1 = int(list1[i])
        else:
            n1 = 0
            
        # Part B: Get value for v2
        if i < len(list2):
            n2 = int(list2[i])
        else:
            n2 = 0
            
        # 4. THE COMPARISON
        if n1 > n2:
            return 1   # v1 is newer
        if n1 < n2:
            return -1  # v2 is newer
            
    # 5. THE DRAW
    # If we finish the loop and never returned, they are identical
    return 0

# --- TEST CHECKS ---
print(f"Test 1 (Simple): {compare_versions('1.2', '1.10')}")     # Should be -1
print(f"Test 2 (Uneven): {compare_versions('1.2.1', '1.2')}")    # Should be 1
print(f"Test 3 (Equal): {compare_versions('1.0', '1.0.0')}")     # Should be 0
