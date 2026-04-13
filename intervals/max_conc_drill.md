# max_conc.py — Drill Notes

## Opening line (say this first)
"This is a sweep line approach. Instead of comparing intervals directly, I
decompose each one into two timestamped events — an arrival and a departure —
then walk through them in order and track the running count."

---

## Algorithm name
**Sweep Line** (also called line sweep or event-based scanning)

---

## How to walk through it out loud
1. For each interval, emit two events: (start, +1) and (end, -1).
2. Sort all events chronologically.
3. Walk through the sorted list, applying each +1 or -1 to a running counter.
4. Track the highest value that counter ever reaches — that's the answer.

---

## The inline trace (use this when explaining)
Input: [[1, 5], [2, 4]]

Events after sort: (1, +1), (2, +1), (4, -1), (5, -1)

| Time | Change | Current | Peak |
|------|--------|---------|------|
| 1    | +1     | 1       | 1    |
| 2    | +1     | 2       | 2    |
| 4    | -1     | 1       | 2    |
| 5    | -1     | 0       | 2    |

Answer: 2

---

## Complexity
- **Time:** O(n log n) — dominated by the sort
- **Space:** O(n) — the events list is 2x the input size

---

## Subtle thing to know about the sort
Events are tuples: `(time, +1 or -1)`. Python sorts tuples left to right.
At a tie on time, `-1 < +1`, so **end events sort before start events**.

This means: if one interval ends at 4 and another starts at 4, the departure
is processed first. They are **not** counted as concurrent.

This is the half-open interval interpretation: [start, end).

**Be ready to say:** "I made a deliberate choice here — end events at the same
timestamp are processed before start events, so touching intervals don't count
as overlapping."

---

## Likely interviewer follow-ups
- "What's the time complexity?" → O(n log n) for the sort
- "What if two events happen at the same time?" → end processes before start;
  explain the tuple sort tie-breaking
- "Why not just compare every pair of intervals?" → that's O(n²), sweep line
  is O(n log n)
- "What does 'sweep line' mean?" → you scan a conceptual vertical line from
  left to right across a timeline, processing events as you hit them
