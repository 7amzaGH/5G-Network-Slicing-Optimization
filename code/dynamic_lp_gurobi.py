"""
Dynamic Resource Allocation using Gurobi
Matches the implementation from the thesis (Listing 1)
"""
import gurobipy as gp
from gurobipy import GRB

# Define sets
S = ['slice1', 'slice2', 'slice3']
L = ['link1', 'link2']
T = ['1', '2']

# Demand dictionary
D = {
    'slice1': {'1': 5, '2': 3},
    'slice2': {'1': 3, '2': 1},
    'slice3': {'1': 1, '2': 3}
}

# Capacity dictionary
C = {'link1': 5, 'link2': 4}

# Create model
m = gp.Model("MaximizeAllocatedBandwidth")

# Decision variables
x = m.addVars(S, L, T, vtype=GRB.BINARY, name="x")

# Objective function
m.setObjective(
    gp.quicksum(x[s, l, t] for s in S for l in L for t in T),
    GRB.MAXIMIZE
)

# Capacity constraints
for l in L:
    for t in T:
        m.addConstr(
            gp.quicksum(x[s, l, t] for s in S) <= C[l],
            f"Capacity_Constraint_{l}_{t}"
        )

# Demand constraints
for s in S:
    for t in T:
        m.addConstr(
            gp.quicksum(x[s, l, t] for l in L) <= D[s][t],
            f"Demand_Constraint_{s}_{t}"
        )

# Optimize
m.optimize()

# Display results
if m.status == GRB.OPTIMAL:
    print("\n" + "="*50)
    print("OPTIMAL SOLUTION FOUND")
    print("="*50)
    for s in S:
        for l in L:
            for t in T:
                if x[s, l, t].X > 0.5:  # Binary variable is 1
                    print(f"Allocated bandwidth of {s} on {l} at time interval {t}: YES")
    print(f"\nTotal Allocated Bandwidth: {m.objVal} Mbps")
    print("="*50)
else:
    print("Model is infeasible or not optimal. Status code:", m.status)
