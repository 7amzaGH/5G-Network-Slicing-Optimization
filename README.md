# Resource Optimization in 5G Network Slicing 📡

### Overview
This project explores **dynamic resource allocation in 5G network slicing**, focusing on optimizing bandwidth allocation using **Integer Linear Programming (ILP)**.  
The work was completed as part of my **Bachelor’s thesis in Computer Science** at the **University of Ain Temouchent (2022/2023)**.

### Objectives
- Analyze 5G architecture, SDN, and NFV frameworks.
- Develop an ILP model for dynamic and fair resource allocation.
- Implement and test the model using **Gurobi**, **Mininet**, and **FlowVisor**.
- Demonstrate fairness and efficiency improvements in network slicing.

### Implementation
- **Modeling Language:** AMPL & Python (Gurobi)
- **Simulation Tools:** Mininet, FlowVisor for SDN slicing
- **Optimization Techniques:** Linear Programming (LP), Integer Linear Programming (ILP)
- **Libraries Used:** Gurobi, PuLP, NumPy

### Example Code Snippet
```python
import gurobipy as gp
from gurobipy import GRB

# Define sets
S = ['slice1', 'slice2', 'slice3']
L = ['link1', 'link2']
T = ['1', '2']

# Model
m = gp.Model("MaximizeBandwidth")
x = m.addVars(S, L, T, vtype=GRB.BINARY, name="x")
m.setObjective(gp.quicksum(x[s, l, t] for s in S for l in L for t in T), GRB.MAXIMIZE)
m.optimize()
