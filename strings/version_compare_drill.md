# version_compare.py — Drill Notes

## Opening line (say this first)
"I split each version string on dots and compare segment by segment. If the
versions have different numbers of segments, I treat the missing ones as zero.
Within each segment, I check for a hyphen to detect pre-release labels — a
version with a beta tag is considered older than the same version without one."

---

## Category
**String parsing / simulation** — no standard algorithm name; shows you can
decompose a spec into clean logic.

---

## How to walk through it out loud
1. Split both strings on `"."` to get a list of segments.
2. Loop up to `max(len(a), len(b))` times.
3. For each position, grab the segment or `"0"` if that version is shorter.
4. Check each segment for a `"-"` (beta tag) using `"in"`.
5. Parse the numeric part by splitting on `"-"` and taking index 0.
6. Compare numerically. If equal, apply the beta tie-breaker: the one with a
   hyphen is older.
7. If all segments are equal, return 0.

---

## Return value contract
| Return | Meaning          |
|--------|------------------|
| 1      | version_a is newer |
| -1     | version_b is newer |
| 0      | they are equal   |

This is the standard comparator contract (same as Java's `compareTo`, Python's
`__lt__/__gt__` internals). Worth naming if asked.

---

## Worked example to say out loud
`"1.2.0-beta"` vs `"1.1.9"`

- Segment 0: `1` vs `1` → equal, no beta tag → continue
- Segment 1: `2` vs `1` → 2 > 1 → return **1** (a is newer)

Beta tag never comes into play here because the numeric comparison resolves it
first. This is correct: even a beta of 1.2 is newer than a released 1.1.

---

## Complexity
- **Time:** O(n) — n being the number of segments (usually tiny, like 3-4)
- **Space:** O(n) — the two split lists

---

## Known limitation (have a sentence ready)
Only handles a single `-beta` style suffix. Doesn't rank among multiple
pre-release types (alpha, beta, rc1, rc2).

**What to say:** "I'd extend this if I needed to rank pre-release types — I'd
probably assign each label a numeric priority and compare those instead of just
checking presence/absence of a hyphen."

---

## Likely interviewer follow-ups
- "What if the versions have different lengths?" → handled — missing segments
  default to `"0"`
- "What if there are multiple beta stages, like rc1 vs rc2?" → acknowledge the
  limitation, explain how you'd extend it
- "Why return 1/-1/0 instead of True/False?" → comparator pattern; lets callers
  know which one is newer, not just whether they differ
- "Could you use Python's built-in sort for this?" → not directly, because
  `"1.10"` sorts before `"1.9"` lexicographically; you need numeric comparison,
  which is exactly what this does
