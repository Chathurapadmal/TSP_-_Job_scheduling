def solve_job_scheduling(jobs, max_deadline):
    # Sort jobs by penalty in descending order so high-penalty jobs are placed first
    jobs = sorted(jobs, key=lambda x: x[2], reverse=True)

    # Track time slots (0 to max_deadline - 1)
    result = [None] * max_deadline
    unscheduled_penalty = 0

    for job in jobs:
        job_id, deadline, penalty = job
        # Try to find the latest available slot on or before the deadline
        placed = False
        for slot in range(min(max_deadline, deadline) - 1, -1, -1):
            if result[slot] is None:
                result[slot] = job_id
                placed = True
                break

        if not placed:
            unscheduled_penalty += penalty

    scheduled_jobs = [res for res in result if res is not None]
    return scheduled_jobs, unscheduled_penalty

def get_jobs_from_user():
    print("Schedule jobs.\n")
    
    # Get number of jobs
    while True:
        try:
            num_jobs = int(input("Enter the number of jobs: "))
            if num_jobs < 1:
                print("Please enter a number >= 1")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    
    # Get max deadline
    while True:
        try:
            max_deadline = int(input("Enter the maximum deadline (number of time slots): "))
            if max_deadline < 1:
                print("Please enter a number >= 1")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
    
    job_list = []
    print(f"\nEnter details for each of the {num_jobs} jobs:")
    
    for i in range(num_jobs):
        print(f"\nJob {i+1}:")
        
        # Get job name
        job_name = input(f"  Enter job name: ").strip()
        if not job_name:
            job_name = f"J{i+1}"
        
        # Get deadline
        while True:
            try:
                deadline = int(input(f"  Enter deadline (1 to {max_deadline}): "))
                if 1 <= deadline <= max_deadline:
                    break
                print(f"  Please enter a value between 1 and {max_deadline}")
            except ValueError:
                print("  Please enter a valid integer")
        
        # Get penalty
        while True:
            try:
                penalty = float(input(f"  Enter penalty/value: "))
                if penalty >= 0:
                    break
                print("  Please enter a non-negative value")
            except ValueError:
                print("  Please enter a valid number")

        job_list.append((job_name, deadline, penalty))
    
    return job_list, max_deadline

# Get user input
job_list, max_deadline = get_jobs_from_user()

# Solve job scheduling
print("\nGenerating optimal schedule...")
schedule, penalty = solve_job_scheduling(job_list, max_deadline)
print(f"\nOptimal Schedule: {schedule}")
print(f"Total Penalty of Unscheduled Jobs: {penalty}")