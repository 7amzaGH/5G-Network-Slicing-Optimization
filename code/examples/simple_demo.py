"""
simple_demo.py
Author: Hamza Ghitri
Description:
    Integer Linear Programming model for dynamic resource optimization in 5G network slicing.
    The goal is to maximize bandwidth utilization across multiple network slices while ensuring fairness.
"""
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# -------------------------------
# Define data
# -------------------------------
slices = ["slice1", "slice2", "slice3"]
links = ["link1", "link2"]
time_slots = [1, 2]

# Link capacity (Mbps)
capacity = {"link1": 100, "link2": 120}

# Slice demand per link per time slot
demand = {
    ("slice1", "link1", 1): 50,
    ("slice1", "link2", 1): 40,
    ("slice1", "link1", 2): 30,  # Added time slot 2
    ("slice1", "link2", 2): 35,
    
    ("slice2", "link1", 1): 30,
    ("slice2", "link2", 1): 60,
    ("slice2", "link1", 2): 40,  # Added time slot 2
    ("slice2", "link2", 2): 50,
    
    ("slice3", "link1", 1): 40,
    ("slice3", "link2", 1): 50,
    ("slice3", "link1", 2): 45,  # Added time slot 2
    ("slice3", "link2", 2): 40,
}

# -------------------------------
# Define model
# -------------------------------
model = LpProblem("5G_Network_Slicing_Optimization", LpMaximize)

# Decision variable: x[slice, link, t] = 1 if bandwidth allocated, 0 otherwise
x = LpVariable.dicts("x", (slices, links, time_slots), cat="Binary")

# Objective: maximize total allocated bandwidth across all time slots
model += lpSum(
    demand.get((s, l, t), 0) * x[s][l][t] 
    for s in slices 
    for l in links 
    for t in time_slots
), "TotalBandwidth"

# Constraints: total usage per link per time slot <= capacity
for l in links:
    for t in time_slots:
        model += (
            lpSum(demand.get((s, l, t), 0) * x[s][l][t] for s in slices) <= capacity[l], 
            f"Capacity_{l}_T{t}"
        )

# Fairness constraint: each slice must get at least one allocation per time slot
for s in slices:
    for t in time_slots:
        model += (
            lpSum(x[s][l][t] for l in links) >= 1, 
            f"Fairness_{s}_T{t}"
        )

# -------------------------------
# Solve
# -------------------------------
print("=" * 50)
print("5G NETWORK SLICING OPTIMIZATION")
print("=" * 50)
print("\nSolving the model...\n")

status = model.solve()

# -------------------------------
# Results
# -------------------------------
print("Status:", "Optimal" if status == 1 else "Not Optimal")
print(f"Solver: {model.solver}")
print("\n" + "=" * 50)
print("ALLOCATION RESULTS")
print("=" * 50)

total_bandwidth = 0
for t in time_slots:
    print(f"\n Time Slot {t}:")
    print("-" * 40)
    for s in slices:
        allocated = []
        for l in links:
            if value(x[s][l][t]) == 1:
                bw = demand.get((s, l, t), 0)
                allocated.append(f"{l}: {bw} Mbps")
                total_bandwidth += bw
        if allocated:
            print(f"  {s:10} → {', '.join(allocated)}")

print("\n" + "=" * 50)
print(f" Total Optimized Bandwidth: {total_bandwidth} Mbps")
print(f" Objective Value: {value(model.objective)}")
print("=" * 50)
