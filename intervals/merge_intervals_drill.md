# merge_intervals.py — Drill Notes

## Opening line (say this first)
"This is also a sweep line approach, but instead of tracking a peak count, I'm watching for when the 'room' empties. Each time it goes from occupied to zero, I've found the end of a merged interval."

---

## Algorithm name
**Sweep Line** — same family as max_conc, different output

---

## How to walk through it out loud
1. For each interval, emit two events: (start, 0) and (end, 1). — 0 for start, 1 for end (this controls tie-breaking, explained below).
2. Sort all events.
3. Walk through events tracking `current_active` (how many intervals are open).
4. When `current_active` is 0 and a start event fires → record the start time.
5. When `current_active` drops back to 0 → close the merged interval, save it.

---

## The encoding choice (0 and 1, not +1 and -1)
In max_conc, events are `(time, +1/-1)`. Here they are `(time, 0/1)`. This flips the tie-breaking:

- max_conc: at time 4, end `(4, -1)` sorts before start `(4, +1)` → not concurrent
- merge_intervals: at time 4, start `(4, 0)` sorts before end `(4, 1)` → they **do** merge

**This is intentional.** Touching endpoints like [1,4] and [4,5] should merge into [1,5]. Test 2 in the file confirms it.

**Be ready to say:** "I used 0 for start and 1 for end specifically so that when two events share a timestamp, starts are processed before ends — that makes touching intervals merge correctly."

---

## Complexity
- **Time:** O(n log n) — dominated by the sort
- **Space:** O(n) — events list plus the merged output

---

## Contrast with max_conc (if asked)

| | max_conc | merge_intervals |
|-|----------|-----------------|
| Goal | find the peak count | find contiguous groups |
| Events | (time, +1/-1) | (time, 0/1) |
| Tie-breaking | end before start | start before end |
| Touching intervals | not concurrent | do merge |

---

## Likely interviewer follow-ups
- "What's the time complexity?" → O(n log n)
- "What if the input isn't sorted?" → doesn't matter, you sort the events yourself
- "Why not sort the intervals directly and scan?" → valid alternative; sketch it: sort by start time, walk and extend the last merged interval if there's overlap. Same O(n log n) complexity, slightly simpler code.
- "What's the difference between this and the max concurrency problem?" → same events idea, different question: peak count vs. merged spans
