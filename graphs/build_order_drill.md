# build_order.py — Drill Notes

## Opening line (say this first)
"This is topological sort using Kahn's algorithm. The idea is: track how many
prerequisites each task is still waiting on, then process tasks in waves as
those counts hit zero."

---

## Algorithm name
**Topological Sort** — Kahn's Algorithm (BFS-based)

---

## Vocabulary to use (not your names, these names)
| Your name       | Standard CS term     |
|-----------------|----------------------|
| Wait Count      | **in-degree**        |
| Unlock Map      | **adjacency list**   |
| ready_to_run_queue | **queue** (BFS)   |

---

## How to walk through it out loud
1. Build the in-degree count and adjacency list from the dependency pairs.
2. Seed the queue with every task whose in-degree is 0 (no prerequisites).
3. Pop a task, append it to the result, then decrement the in-degree of everything it unlocks.
4. If a dependent's in-degree just hit 0, add it to the queue.
5. After the loop: if the result length equals total tasks, success. If not, there was a cycle.

---

## Complexity
- **Time:** O(V + E) — each task (vertex) and each dependency (edge) touched once.
- **Space:** O(V + E) — storing the adjacency list and in-degree map.

---

## The bug to know about
```python
current_task = ready_to_run_queue.pop(0)  # O(n) — shifts the whole list
```
Fix: use `collections.deque` and call `.popleft()` instead (O(1)).

**What to say:** "I'd swap the list for a `collections.deque` to get O(1) pops
from the front."

---

## Cycle detection — how it works
If A waits for B and B waits for A, neither ever reaches in-degree 0. They
never enter the queue, never get appended to the result. So the result ends up
shorter than the full task list — that's the signal.

---

## Likely interviewer follow-ups
- "What's the time complexity?" → O(V + E)
- "What if there's a cycle?" → return empty list; explain the length check
- "Why pop(0) instead of deque?" → acknowledge it, say you'd use deque
- "What does topological sort guarantee?" → that every prerequisite appears
  before the tasks that depend on it
