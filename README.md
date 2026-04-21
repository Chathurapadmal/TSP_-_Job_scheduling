

# Advanced Mathematics: Optimization Algorithms

This repository contains Python implementations for two classic optimization problems: the **Traveling Salesman Problem (TSP)** and the **Job Scheduling Problem with Deadlines and Penalties**. [cite_start]These projects were developed to demonstrate the bridge between mathematical theory and algorithmic implementation[cite: 42, 124, 639].

## 1. Traveling Salesman Problem (TSP)

### About the Project
[cite_start]The TSP is an NP-hard problem in combinatorial optimization[cite: 4]. [cite_start]The goal is to find the shortest possible route that starts at a specific origin city, visits every other city exactly once, and returns to the starting point[cite: 5, 6, 7].

### The Code Logic
[cite_start]The implementation uses a **Brute-Force approach** with permutations to guarantee the absolute shortest path[cite: 52, 109].

* [cite_start]**Permutations:** Using `itertools.permutations`, the code generates every possible visiting order for the cities[cite: 119].
* [cite_start]**Distance Matrix:** Distances are stored in a 2D array (`distance_matrix[i][j]`), where the value represents the distance from city $i$ to city $j$[cite: 15, 143].
* [cite_start]**Cyclic Calculation:** The algorithm fixes City 0 as the origin to reduce redundant calculations and ensures the route always returns to the start[cite: 98, 120].
* **Mathematical Objective:**
    [cite_start]$$\text{Minimize } \sum_{i=0}^{n-1} d(c_i, c_{i+1}) \text{ where } c_n = c_0$$[cite: 125].

---

## 2. Job Scheduling with Deadlines and Penalties

### About the Project
[cite_start]This project solves the problem of scheduling $n$ jobs on a single processor to minimize the total penalty incurred from missed deadlines[cite: 318, 516]. [cite_start]Each job takes exactly one unit of time to complete[cite: 326, 514].

### The Code Logic
[cite_start]The solution implements a **Greedy Strategy**, which is highly efficient for this specific problem type[cite: 347, 538].

* [cite_start]**Priority Sorting:** Jobs are sorted in descending order based on their **penalty** values[cite: 353, 550]. [cite_start]This ensures that "expensive" jobs are given priority[cite: 540, 555].
* [cite_start]**Latest Slot Allocation:** For each job, the code searches for the **latest available time slot** before or at its deadline[cite: 355, 420].
    * [cite_start]*Why latest?* By occupying the latest possible slot, we keep earlier slots open for jobs with tighter (earlier) deadlines, maximizing the total number of scheduled jobs[cite: 366, 545, 583].
* [cite_start]**Penalty Accumulation:** If no valid slot is found, the job is marked as unscheduled, and its penalty is added to the total[cite: 359, 597].

---

## Technical Stack
* **Language:** Python 3.x
* **Libraries:** `itertools` (for TSP permutations)
* **Platform:** Developed and tested on Arch Linux

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/optimization-algorithms.git
   ```
2. Run the scripts:
   ```bash
   python tsp_solver.py
   python job_scheduler.py
   ```

---


