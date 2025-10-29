"""
dynamic_lp.py
Author: Hamza Ghitri
Description:
    Integer Linear Programming model for dynamic resource optimization in 5G network slicing.
    The goal is to maximize bandwidth utilization across multiple network slices while ensuring fairness.
"""

from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# -------------------------------
# Define data
# -------------------------------
slices = ["slice1", "slice2", "slice3"]
links = ["link1", "link2"]
time_slots = [1, 2]

# Link capacity (example Mbps)
capacity = {"link1": 100, "link2": 120}

# Slice demand per link per time slot
demand = {
    ("slice1", "link1", 1): 50,
    ("slice1", "link2", 1): 40,
    ("slice2", "link1", 1): 30,
    ("slice2", "link2", 1): 60,
    ("slice3", "link1", 1): 40,
    ("slice3", "link2", 1): 50,
}

# -------------------------------
# Define model
# -------------------------------
model = LpProblem("5G_Network_Slicing_Optimization", LpMaximize)

# Decision variable: x[slice, link, t] = 1 if bandwidth allocated, 0 otherwise
x = LpVariable.dicts("x", (slices, links, time_slots), cat="Binary")

# Objective: maximize total allocated bandwidth
model += lpSum(demand[(s, l, 1)] * x[s][l][1] for s in slices for l in links), "TotalBandwidth"

# Constraints: total usage per link <= capacity
for l in links:
    model += lpSum(demand[(s, l, 1)] * x[s][l][1] for s in slices) <= capacity[l], f"Cap_{l}"

# Fairness constraint: each slice must get at least one active link
for s in slices:
    model += lpSum(x[s][l][1] for l in links) >= 1, f"Fairness_{s}"

# -------------------------------
# Solve
# -------------------------------
model.solve()

# -------------------------------
# Results
# -------------------------------
print("Status:", model.status)
for s in slices:
    for l in links:
        if x[s][l][1].value() == 1:
            print(f"Slice {s} uses {l}")

print("Total optimized bandwidth:", model.objective.value())
