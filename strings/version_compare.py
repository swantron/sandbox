def compare_versions_with_beta(version_a: str, version_b: str) -> int:
    # 1. DECONSTRUCTION
    segments_a = version_a.split(".")
    segments_b = version_b.split(".")
    
    total_segments = max(len(segments_a), len(segments_b))
    
    for i in range(total_segments):
        # A. Get the raw string segments (or "0" if missing)
        raw_a = segments_a[i] if i < len(segments_a) else "0"
        raw_b = segments_b[i] if i < len(segments_b) else "0"

        # B. THE BETA CHECK: Look for hyphens
        # "0-beta" vs "0"
        has_beta_a = "-" in raw_a
        has_beta_b = "-" in raw_b

        # C. Extract the purely numeric part for comparison
        # "1-beta".split("-")[0] gives us "1"
        num_a = int(raw_a.split("-")[0])
        num_b = int(raw_b.split("-")[0])

        # D. Compare the numbers first
        if num_a > num_b: return 1
        if num_b > num_a: return -1

        # E. TIE-BREAKER: Numbers are equal, but does one have a beta tag?
        # Rule: A version WITH a hyphen is OLDER than the same version WITHOUT.
        if has_beta_a and not has_beta_b:
            return -1 # a is a beta, b is final -> b wins
        if not has_beta_a and has_beta_b:
            return 1  # a is final, b is beta -> a wins
            
    return 0

# --- READABLE TEST SUITE ---
print(f"1.2.0-beta vs 1.2.0: {compare_versions_with_beta('1.2.0-beta', '1.2.0')}") 
# Expected: -1 (Beta is older)

print(f"1.2.0-beta vs 1.1.9: {compare_versions_with_beta('1.2.0-beta', '1.1.9')}")
# Expected: 1 (Even a beta of 1.2 is newer than 1.1)