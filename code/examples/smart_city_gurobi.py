"""
Smart City 5G Network Slicing using Gurobi
Real-world scenario: 5 slices, 4 links, 24 hours
"""
import gurobipy as gp
from gurobipy import GRB

# -------------------------------
# Define data
# -------------------------------
slices = ["eMBB", "uRLLC", "mMTC", "PublicSafety", "VideoSurveillance"]
links = ["fiber", "microwave", "mmwave", "sub6ghz"]
time_slots = list(range(1, 25))  # 24 hours

# Link capacities (Mbps)
capacity = {
    "fiber": 10000,
    "microwave": 2000,
    "mmwave": 5000,
    "sub6ghz": 3000
}

# Realistic hourly demands (Mbps)
embb_pattern = [200, 150, 100, 80, 100, 300, 800, 1200, 1000, 600, 500, 600,
                700, 650, 700, 900, 1500, 1800, 1400, 900, 600, 400, 300, 250]

urllc_pattern = [50, 30, 20, 20, 40, 150, 400, 600, 500, 300, 250, 280,
                 300, 280, 300, 350, 700, 800, 600, 350, 200, 120, 80, 60]

mmtc_pattern = [100, 95, 90, 88, 90, 100, 110, 120, 115, 105, 100, 105,
                110, 108, 110, 115, 125, 130, 120, 110, 105, 102, 100, 98]

public_safety_pattern = [50, 50, 50, 50, 50, 60, 70, 80, 75, 65, 60, 65,
                         70, 68, 70, 75, 85, 90, 85, 75, 65, 60, 55, 50]

video_pattern = [300, 350, 400, 450, 400, 350, 280, 250, 230, 220, 210, 215,
                 220, 215, 220, 240, 260, 280, 300, 350, 380, 360, 340, 320]

# Build demand dictionary
demand = {}

for t in time_slots:
    idx = t - 1
    
    # eMBB distribution
    demand[("eMBB", "fiber", t)] = int(embb_pattern[idx] * 0.5)
    demand[("eMBB", "mmwave", t)] = int(embb_pattern[idx] * 0.3)
    demand[("eMBB", "sub6ghz", t)] = int(embb_pattern[idx] * 0.2)
    demand[("eMBB", "microwave", t)] = 0
    
    # uRLLC distribution
    demand[("uRLLC", "fiber", t)] = int(urllc_pattern[idx] * 0.6)
    demand[("uRLLC", "mmwave", t)] = int(urllc_pattern[idx] * 0.4)
    demand[("uRLLC", "sub6ghz", t)] = 0
    demand[("uRLLC", "microwave", t)] = 0
    
    # mMTC distribution
    demand[("mMTC", "fiber", t)] = int(mmtc_pattern[idx] * 0.3)
    demand[("mMTC", "microwave", t)] = int(mmtc_pattern[idx] * 0.2)
    demand[("mMTC", "mmwave", t)] = int(mmtc_pattern[idx] * 0.2)
    demand[("mMTC", "sub6ghz", t)] = int(mmtc_pattern[idx] * 0.3)
    
    # PublicSafety distribution
    demand[("PublicSafety", "fiber", t)] = int(public_safety_pattern[idx] * 0.7)
    demand[("PublicSafety", "microwave", t)] = int(public_safety_pattern[idx] * 0.3)
    demand[("PublicSafety", "mmwave", t)] = 0
    demand[("PublicSafety", "sub6ghz", t)] = 0
    
    # VideoSurveillance distribution
    demand[("VideoSurveillance", "fiber", t)] = int(video_pattern[idx] * 0.6)
    demand[("VideoSurveillance", "sub6ghz", t)] = int(video_pattern[idx] * 0.4)
    demand[("VideoSurveillance", "mmwave", t)] = 0
    demand[("VideoSurveillance", "microwave", t)] = 0

# -------------------------------
# Create Gurobi Model
# -------------------------------
print("="*60)
print("5G SMART CITY NETWORK SLICING - GUROBI OPTIMIZATION")
print("="*60)
print("\nBuilding optimization model...")

m = gp.Model("SmartCity_5G_Slicing")

# Suppress Gurobi output (optional)
m.setParam('OutputFlag', 0)

# Decision variables
x = m.addVars(slices, links, time_slots, vtype=GRB.BINARY, name="allocation")

# Objective: maximize total allocated bandwidth
m.setObjective(
    gp.quicksum(demand.get((s, l, t), 0) * x[s, l, t] 
                for s in slices for l in links for t in time_slots),
    GRB.MAXIMIZE
)

# Capacity constraints
for l in links:
    for t in time_slots:
        m.addConstr(
            gp.quicksum(demand.get((s, l, t), 0) * x[s, l, t] for s in slices) <= capacity[l],
            f"Capacity_{l}_T{t}"
        )

# Fairness constraints
for s in slices:
    for t in time_slots:
        m.addConstr(
            gp.quicksum(x[s, l, t] for l in links) >= 1,
            f"Fairness_{s}_T{t}"
        )

# -------------------------------
# Optimize
# -------------------------------
print("Solving the model...\n")
m.optimize()

# -------------------------------
# Display Results
# -------------------------------
if m.status == GRB.OPTIMAL:
    print("Status: OPTIMAL")
    print(f"Solver: Gurobi Optimizer v{gp.gurobi.version()}")
    print(f"Solution Time: {m.Runtime:.2f} seconds\n")
    
    print("="*60)
    print("ALLOCATION RESULTS")
    print("="*60)
    
    total_bandwidth = 0
    
    for t in time_slots:
        print(f"\n Time Slot {t}:")
        print("-" * 50)
        for s in slices:
            allocated = []
            for l in links:
                if x[s, l, t].X > 0.5:  # Binary is 1
                    bw = demand.get((s, l, t), 0)
                    allocated.append(f"{l}: {bw} Mbps")
                    total_bandwidth += bw
            if allocated:
                print(f"  {s:20} → {', '.join(allocated)}")
    
    print("\n" + "="*60)
    print(f" Total Optimized Bandwidth: {total_bandwidth:,} Mbps")
    print(f" Objective Value: {m.objVal:,.1f}")
    print(f" Peak Utilization: {(total_bandwidth/(sum(capacity.values())*24))*100:.1f}%")
    print("="*60)
    
else:
    print(f" Optimization failed!")
    print(f"Status: {m.status}")
