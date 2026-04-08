def get_build_order(tasks, dependencies):
    # 1. Setup our "Wait-Lists" and "Unlock-Maps"
    # Every task starts waiting for 0 things
    wait_count = {t: 0 for t in tasks}
    # Every task starts with nobody to unlock
    unlock_map = {t: [] for t in tasks}

    # 2. Fill the data from the dependencies list
    # (task, prereq) means 'task' is waiting for 'prereq'
    for task, prereq in dependencies:
        wait_count[task] += 1
        unlock_map[prereq].append(task)

    # 3. Find the tasks that are ready to go RIGHT NOW (waiting for 0)
    # We call this the "Queue"
    queue = [t for t in tasks if wait_count[t] == 0]
    
    build_order = []

    # 4. The Process: "Do work, Unlock neighbors"
    while queue:
        # Take a task that is ready
        current = queue.pop(0)
        build_order.append(current)

        # Look at everyone waiting for this task to finish
        for dependent in unlock_map[current]:
            # They are now waiting for one less thing!
            wait_count[dependent] -= 1
            
            # If they aren't waiting for anything else, they are ready!
            if wait_count[dependent] == 0:
                queue.append(dependent)

    # 5. The Final Check: Did we get stuck in a circle?
    if len(build_order) == len(tasks):
        return build_order
    else:
        return [] # Circular dependency detected
