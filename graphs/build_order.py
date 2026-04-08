def find_execution_order(tasks, dependencies):
    # --- STEP 1: INITIALIZE THE "LOCKERS" (Dictionaries) ---
    
    # "Wait Count" is a dictionary of numbers. 
    # Key: Task Name | Value: How many things it is currently waiting for.
    # Initially, everyone is waiting for 0 things.
    wait_count = {task_name: 0 for task_name in tasks}
    
    # "Unlock Map" is a dictionary of lists.
    # Key: Task Name | Value: A list of people to notify when this task finishes.
    # Initially, every task has an empty notification list [].
    unlock_map = {task_name: [] for task_name in tasks}

    # --- STEP 2: FILL THE LOCKERS FROM THE DEPENDENCIES ---
    # A dependency pair is (the_blocked_task, the_prerequisite)
    for blocked_task, prerequisite in dependencies:
        
        # Increment the count in the blocked_task's "Wait Locker"
        wait_count[blocked_task] = wait_count[blocked_task] + 1
        
        # Add the blocked_task to the prerequisite's "Notification List"
        unlock_map[prerequisite].append(blocked_task)

    # 

    # --- STEP 3: FIND THE "READY" TASKS ---
    # We look through every task's "Wait Locker". 
    # If the number is 0, they are ready to run immediately.
    ready_to_run_queue = [name for name in tasks if wait_count[name] == 0]
    
    # This list will hold our final, safe sequence of tasks
    final_build_sequence = []

    # --- STEP 4: THE PROCESSING LOOP ---
    # While there is at least one task ready to run...
    while len(ready_to_run_queue) > 0:
        
        # 1. "Perform" the task (Remove it from the ready list)
        current_task = ready_to_run_queue.pop(0)
        final_build_sequence.append(current_task)

        # 2. "Unlock" the dependents
        # Look at the "Notification List" for the task we just finished
        list_of_people_to_notify = unlock_map[current_task]
        
        for dependent_name in list_of_people_to_notify:
            # Reach into that person's "Wait Locker" and subtract 1
            wait_count[dependent_name] = wait_count[dependent_name] - 1
            
            # 3. "Check" if they are now ready
            # If their "Wait Locker" just hit 0, they can move to the Ready list!
            if wait_count[dependent_name] == 0:
                ready_to_run_queue.append(dependent_name)

    # --- STEP 5: THE FINAL VALIDATION ---
    # If our final sequence has the same number of tasks we started with, it's a success.
    # If not, some tasks were stuck in a circular dependency (A waits for B, B waits for A).
    if len(final_build_sequence) == len(tasks):
        return final_build_sequence
    else:
        # Return an empty list to signal a "Borked" build
        return []

# --- VERBOSE TEST CHECKS ---

# Test 1: A Linear Chain (A depends on B, B depends on C)
# Correct Order: C -> B -> A
print(f"Test 1 (Linear Chain): {find_execution_order(['A', 'B', 'C'], [('A', 'B'), ('B', 'C')])}")

# Test 2: Parallel Independence (B and C both depend on A)
# Correct Order: A must be first, then B and C (in any order)
print(f"Test 2 (Parallel): {find_execution_order(['A', 'B', 'C'], [('B', 'A'), ('C', 'A')])}")

# Test 3: The Circular Dependency (The Loop)
# A depends on B, B depends on A. No one can ever start.
print(f"Test 3 (Circular): {find_execution_order(['A', 'B'], [('A', 'B'), ('B', 'A')])}")

# Test 4: The "Diamond" (A depends on B and C, both B and C depend on D)
# Correct Order: D must be first, then B/C, then A last.
tasks_list = ['A', 'B', 'C', 'D']
deps_list = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]
print(f"Test 4 (Diamond): {find_execution_order(tasks_list, deps_list)}")