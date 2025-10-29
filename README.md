# Resource Optimization in 5G Network Slicing 📡

## 📁 Repository Structure
```
├── code/
│   ├── examples/
│   │   ├── simple_demo.py             # PuLP implementation (basic)
│   │   ├── simple_demo_gurobi.py      # Gurobi implementation (basic)
│   │   ├── smart_city.py              # Smart City scenario (24 hours)
│   │   └── smart_city_gurobi.py       # Smart City with Gurobi (24 hours)
│   ├── models/
│   │   ├── model.mod                  # AMPL model definition
│   │   ├── simple_data.dat            # Data for simple demo
│   │   └── smart_city_data.dat        # Data for Smart City
│   ├── notebooks/
│   │   ├── simple_demo.ipynb          # Interactive simple demo
│   │   └── smart_city.ipynb           # Interactive Smart City demo
│   ├── requirements.txt               # Python dependencies
│   └── README.md       
├── thesis.pdf
├── LICENSE
└── README.md
```

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

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager
- (Optional) Gurobi license for commercial solver
- 
### Installation
```bash
# Clone the repository
git clone https://github.com/7amzaGH/5G-Network-Slicing-Optimization.git
cd 5G-Network-Slicing-Optimization

# Install dependencies
cd code
pip install -r requirements.txt

# Run the model
python dynamic_lp.py
```
## 💻 Usage

### Example 1: Simple Demo (Learning Example)

**Quick 3-slice demonstration** to understand the basics:
```bash
# Using PuLP (open-source)
python code/examples/simple_demo.py

# Using Gurobi (requires license)
python code/examples/simple_demo_gurobi.py

# Interactive Jupyter notebook
jupyter notebook code/notebooks/simple_demo.ipynb
```

**Scenario Details:**
- 3 network slices (slice1, slice2, slice3)
- 2 physical links (link1, link2)
- 2 time slots
- Total: 370 Mbps optimized allocation

---

### Example 2: Smart City (Real-World Scenario)

**Realistic 24-hour smart city deployment:**
```bash
# Using PuLP
python code/examples/smart_city.py

# Using Gurobi (faster for large-scale)
python code/examples/smart_city_gurobi.py

# Interactive visualization notebook
jupyter notebook code/notebooks/smart_city.ipynb
```

**Scenario Details:**
- 5 network slices (eMBB, uRLLC, mMTC, PublicSafety, VideoSurveillance)
- 4 physical links (fiber, microwave, mmWave, sub-6GHz)
- 24 time slots (hourly demands)
- Dynamic traffic patterns (rush hour peaks, night-time lows)
- Total: 33.7 Gbps optimized allocation


---

## 📊 Results

### Simple Demo Results
- **Total Bandwidth:** 370 Mbps
- **Fairness:** All slices allocated in both time slots
- **Efficiency:** 84% average link utilization

### Smart City Scenario (24-Hour Simulation)

The model successfully optimizes bandwidth allocation for a realistic smart city deployment.

**Key Achievements:**
- **Total Bandwidth Allocated:** 33,748 Mbps (33.7 Gbps)
- **Fairness:** All slices guaranteed allocation in every time slot
- **Peak Efficiency:** 92% link utilization during rush hours (7-9am, 5-6pm)
- **Average Efficiency:** 42% daily utilization (reflects realistic off-peak patterns)

**Performance Highlights:**
- **eMBB:** Peaks at 900 Mbps during evening commute (6pm)
- **uRLLC:** Scales from 30 Mbps (night) to 480 Mbps (rush hour)
- **mMTC:** Maintains stable ~100 Mbps (constant IoT sensor traffic)
- **PublicSafety:** Guaranteed 50-89 Mbps across all time periods
- **VideoSurveillance:** 180-270 Mbps with higher allocation during night hours

---

## 🔧 AMPL Usage

For those using AMPL modeling language:
```bash
ampl code/models/model.mod code/models/simple_data.dat
# or
ampl code/models/model.mod code/models/smart_city_data.dat
```

---

## 📄 Full Thesis Report

👉 [Click here to view the full PDF on Google Drive](https://drive.google.com/file/d/1zyUAntguo4mpcDOGxhDmdRMlg2pkiF0p/view?usp=sharing)

## 🚀 Quick Code Preview

**Simple optimization with Gurobi:**
```python
import gurobipy as gp
from gurobipy import GRB

# Define network elements
S = ['slice1', 'slice2', 'slice3']  # Network slices
L = ['link1', 'link2']              # Physical links
T = ['1', '2']                      # Time slots

# Create optimization model
m = gp.Model("5G_Network_Slicing")
x = m.addVars(S, L, T, vtype=GRB.BINARY, name="allocation")

# Objective: Maximize total bandwidth allocation
m.setObjective(gp.quicksum(demand[s,l,t] * x[s,l,t] 
               for s in S for l in L for t in T), GRB.MAXIMIZE)

# Solve
m.optimize()
print(f"Optimal bandwidth: {m.objVal} Mbps")
```

## 👥 Authors

- **Hamza Ghitri** - [GitHub](https://github.com/7amzaGH)
- **Aya Boudaoud** - Co-author

## 🙏 Acknowledgments

Supervised by **Dr. Ali Benzerbadj**  
University of Ain Temouchent Belhadj Bouchaib  
Academic Year: 2022/2023

## 📧 Contact

For questions or collaboration:
- GitHub: [@7amzaGH](https://github.com/7amzaGH)
- Email: your.email@example.com

### Example Code Snippet
**Minimal demo** (3 slices, 2 links, 2 time slots):
```python
import gurobipy as gp
from gurobipy import GRB

# Define network elements
S = ['slice1', 'slice2', 'slice3']  # Network slices
L = ['link1', 'link2']              # Physical links
T = ['1', '2']                      # Time slots

# Create optimization model
m = gp.Model("5G_Network_Slicing")
x = m.addVars(S, L, T, vtype=GRB.BINARY, name="allocation")

# Objective: Maximize total bandwidth allocation
m.setObjective(gp.quicksum(x[s, l, t] for s in S for l in L for t in T), 
               GRB.MAXIMIZE)

# Solve
m.optimize()
print(f"Optimal bandwidth: {m.objVal} Mbps")
```

### Real-World Application
The thesis demonstrates this model applied to:
- **eMBB slices:** Video streaming (high bandwidth)
- **uRLLC slices:** Autonomous vehicles (low latency)
- **mMTC slices:** IoT sensors (massive connections)

With dynamic demands varying across 24-hour periods.
See full thesis for detailed scenarios.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




