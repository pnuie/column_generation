# Column Generation for Cutting Stock Problem

## Overview

This repository implements a Column Generation approach for solving the Cutting Stock Problem (CSP), a classical application of linear programming and combinatorial optimization.  
Starting with a limited set of cutting patterns, the algorithm iteratively solves a restricted master problem and a subproblem to generate new patterns with negative reduced cost, gradually improving the solution.

---

## Problem Description

Given stock material of fixed length $L$ and demands for various smaller item lengths, the goal is to determine the minimum number of stock rolls needed to satisfy the demands.

---

## Approach: Column Generation

1. **Initialization**:  
   - Start with simple cutting patterns (e.g., cutting as many of one type as possible).

2. **Restricted Master Problem**:  
   - Solve a linear program to determine how many times each cutting pattern should be used.

3. **Subproblem (Pricing Problem)**:  
   - Using dual variables from the master problem, solve a knapsack problem to find new cutting patterns with negative reduced cost.

4. **Iteration**:  
   - If a new pattern improves the objective, add it to the master problem and repeat.

5. **Termination**:  
   - Stop when no new improving pattern can be found.

---

## Key Features

- Implemented in **Python** using **Gurobi** optimizer.
- Master problem and subproblem are separated into modular functions.
- Relaxation-based formulation (continuous variables) for faster convergence.
- Automatic generation of new columns (cutting patterns) until optimality is reached.

---

## File Structure

```
/column_generation
 ├── column_generation.py  # Main script implementing the Column Generation method
 ├── README.md             # Project documentation
```

---

## Requirements

- Python 3.x
- Gurobi Optimizer (and `gurobipy` package)

Install Gurobi Python API:
```bash
pip install gurobipy
```

---

