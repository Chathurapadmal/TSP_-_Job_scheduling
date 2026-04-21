

# Advanced Mathematics: Optimization Algorithms

This repository contains Python implementations for two classic optimization problems: the **Traveling Salesman Problem (TSP)** and the **Job Scheduling Problem with Deadlines and Penalties**. These projects were developed to demonstrate the bridge between mathematical theory and algorithmic implementation.

## 1. Traveling Salesman Problem (TSP)

### About the Project
The TSP is an NP-hard problem in combinatorial optimization[cite: 4]. [cite_start]The goal is to find the shortest possible route that starts at a specific origin city, visits every other city exactly once, and returns to the starting point.

### The Code Logic
[cite_start]The implementation uses a **Brute-Force approach** with permutations to guarantee the absolute shortest path.

* **Permutations:** Using `itertools.permutations`, the code generates every possible visiting order for the cities.
* **Distance Matrix:** Distances are stored in a 2D array (`distance_matrix[i][j]`), where the value represents the distance from city $i$ to city $j$.
* **Cyclic Calculation:** The algorithm fixes City 0 as the origin to reduce redundant calculations and ensures the route always returns to the start.
* **Mathematical Objective:**
    $$\text{Minimize } \sum_{i=0}^{n-1} d(c_i, c_{i+1}) \text{ where } c_n = c_0$$.

---

## 2. Job Scheduling with Deadlines and Penalties

### About the Project
This project solves the problem of scheduling $n$ jobs on a single processor to minimize the total penalty incurred from missed deadlines. Each job takes exactly one unit of time to complete.

### The Code Logic
[cite_start]The solution implements a **Greedy Strategy**, which is highly efficient for this specific problem type.

* [cite_start]**Priority Sorting:** Jobs are sorted in descending order based on their **penalty** values. This ensures that "expensive" jobs are given priority.
* [cite_start]**Latest Slot Allocation:** For each job, the code searches for the **latest available time slot** before or at its deadline.
    * [cite_start]*Why latest?* By occupying the latest possible slot, we keep earlier slots open for jobs with tighter (earlier) deadlines, maximizing the total number of scheduled jobs.
* [cite_start]**Penalty Accumulation:** If no valid slot is found, the job is marked as unscheduled, and its penalty is added to the total.

---

## Technical Stack
* **Language:** Python 3.x
* **Libraries:** `itertools` (for TSP permutations)
* **Platform:** Developed and tested on Arch Linux

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Chathurapadmal/TSP_-_Job_scheduling.git
   ```
2. Run the scripts:
   ```bash
   python3 tsp.py
   python3 jobschedule.py
   ```

---


