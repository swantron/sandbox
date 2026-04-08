def find_execution_order(tasks, dependencies):
    # --- STEP 1: INITIALIZE STATE ---
    # wait_count: How many things must finish before I can start?
    wait_count = {task: 0 for task in tasks}
    
    # unlock_map: When I finish, who do I notify?
    unlock_map = {task: [] for task in tasks}

    # --- STEP 2: BUILD THE RELATIONSHIPS ---
    # Each dependency is a pair: (task, prerequisite)
    for task, prereq in dependencies:
        wait_count[task] += 1
        unlock_map[prereq].append(task)

    # --- STEP 3: FIND STARTING POINTS ---
    # Anyone waiting for 0 things is "Ready"
    ready_queue = [task for task in tasks if wait_count[task] == 0]
    
    final_order = []

    # --- STEP 4: THE PROCESSING LOOP ---
    while ready_queue:
        current_task = ready_queue.pop(0)
        final_order.append(current_task)

        for dependent_task in unlock_map[current_task]:
            wait_count[dependent_task] -= 1
            if wait_count[dependent_task] == 0:
                ready_queue.append(dependent_task)

    # --- STEP 5: VALIDATE ---
    if len(final_order) == len(tasks):
        return final_order
    else:
        # If we couldn't process everyone, there's a loop
        return []

# --- TEST CHECKS ---

# Test 1: Linear Chain (C -> B -> A)
# A depends on B, B depends on C
tasks1 = ["A", "B", "C"]
deps1 = [("A", "B"), ("B", "C")]
print(f"Test 1 (Linear): {find_execution_order(tasks1, deps1)}")
# Expected: ['C', 'B', 'A']

# Test 2: Parallel Tasks
# B and C both depend on A. D is lonely.
tasks2 = ["A", "B", "C", "D"]
deps2 = [("B", "A"), ("C", "A")]
print(f"Test 2 (Parallel): {find_execution_order(tasks2, deps2)}")
# Expected: ['A', 'D', 'B', 'C'] (Order of B, C, D can vary)

# Test 3: Circular Dependency (The "Borked" Build)
# A depends on B, B depends on A
tasks3 = ["A", "B"]
deps3 = [("A", "B"), ("B", "A")]
print(f"Test 3 (Circular): {find_execution_order(tasks3, deps3)}")
# Expected: []

# Test 4: Complex Monorepo Style
# A depends on B and C. B depends on D. C depends on D.
tasks4 = ["A", "B", "C", "D"]
deps4 = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D")]
print(f"Test 4 (Complex): {find_execution_order(tasks4, deps4)}")
# Expected: ['D', 'B', 'C', 'A']