"""
Simple Demo using Gurobi
Matches simple_data.dat (3 slices, 2 links, 2 time slots)
"""
import gurobipy as gp
from gurobipy import GRB

# Define sets
S = ['slice1', 'slice2', 'slice3']
L = ['link1', 'link2']
T = ['1', '2']

# Demand dictionary (matches simple_data.dat)
D = {
    'slice1': {'1': {'link1': 50, 'link2': 40}, 
               '2': {'link1': 30, 'link2': 35}},
    'slice2': {'1': {'link1': 30, 'link2': 60}, 
               '2': {'link1': 40, 'link2': 50}},
    'slice3': {'1': {'link1': 40, 'link2': 50}, 
               '2': {'link1': 45, 'link2': 40}}
}

# Capacity dictionary
C = {'link1': 100, 'link2': 120}

# Create model
m = gp.Model("SimpleDemo_5G_Slicing")

# Decision variables
x = m.addVars(S, L, T, vtype=GRB.BINARY, name="x")

# Objective function: maximize total allocated bandwidth
m.setObjective(
    gp.quicksum(D[s][t][l] * x[s, l, t] for s in S for l in L for t in T),
    GRB.MAXIMIZE
)

# Capacity constraints: total bandwidth per link <= capacity
for l in L:
    for t in T:
        m.addConstr(
            gp.quicksum(D[s][t][l] * x[s, l, t] for s in S) <= C[l],
            f"Capacity_{l}_T{t}"
        )

# Fairness constraints: each slice gets at least 1 link per time slot
for s in S:
    for t in T:
        m.addConstr(
            gp.quicksum(x[s, l, t] for l in L) >= 1,
            f"Fairness_{s}_T{t}"
        )

# Optimize
m.optimize()

# Display results
print("\n" + "="*50)
print("SIMPLE DEMO - GUROBI OPTIMIZATION")
print("="*50)

if m.status == GRB.OPTIMAL:
    print(f"\nStatus: OPTIMAL")
    print(f"Solver: Gurobi Optimizer\n")
    
    total_bandwidth = 0
    
    for t in T:
        print(f" Time Slot {t}:")
        print("-" * 40)
        for s in S:
            allocated = []
            for l in L:
                if x[s, l, t].X > 0.5:  # Binary is 1
                    bw = D[s][t][l]
                    allocated.append(f"{l}: {bw} Mbps")
                    total_bandwidth += bw
            if allocated:
                print(f"  {s:10} → {', '.join(allocated)}")
        print()
    
    print("="*50)
    print(f" Total Allocated Bandwidth: {total_bandwidth} Mbps")
    print(f" Objective Value: {m.objVal}")
    print("="*50)
else:
    print(f" Model is infeasible or not optimal.")
    print(f"Status code: {m.status}")
