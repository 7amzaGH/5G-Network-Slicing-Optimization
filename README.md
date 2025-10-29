# Resource Optimization in 5G Network Slicing 📡

## 📁 Repository Structure
```
├── code/
│   ├── dynamic_lp.py          # PuLP implementation
│   ├── model.mod              # AMPL model
│   ├── data.dat               # AMPL data
│   ├── solver_example.ipynb   # Jupyter notebook demo
│   ├── README.md              # Code documentation
│   └── requirements.txt
├── thesis.pdf
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

### Option 1: Python (PuLP)
```bash
python code/dynamic_lp.py
```

### Option 2: Jupyter Notebook
```bash
jupyter notebook code/solver_example.ipynb
```

### Option 3: AMPL
```bash
ampl code/model.mod code/data.dat
```

## 📊 Results

The model optimizes bandwidth allocation achieving:
- **Total Bandwidth:** 370 Mbps
- **Fairness:** Each slice guaranteed minimum allocation
- **Efficiency:** 92% link utilization

![Optimization Results](results/optimization_plot.png)

## 📄 PDF Report

👉 [Click here to view the full PDF on Google Drive](https://drive.google.com/file/d/1zyUAntguo4mpcDOGxhDmdRMlg2pkiF0p/view?usp=sharing)

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
Here's how the optimization model works:
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
**Output:**
```
Optimal bandwidth: 370.0 Mbps
```


