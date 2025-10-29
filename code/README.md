# Code Documentation
```
## 📁 Repository Structure
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
```

---
## 🎯 Available Examples

### 1. Simple Demo (Learning Example)

**Purpose:** Understand the basics of network slicing optimization

**Files:**
- `examples/simple_demo.py` - PuLP implementation
- `examples/simple_demo_gurobi.py` - Gurobi implementation
- `models/simple_data.dat` - AMPL data file
- `notebooks/simple_demo.ipynb` - Interactive notebook

**Run:**
```bash
python examples/simple_demo.py
```

**Scenario:**
- 3 slices, 2 links, 2 time slots
- Small-scale for learning
- Expected output: 370 Mbps total allocation

---

### 2. Smart City (Real-World Scenario)

**Purpose:** Demonstrate realistic 24-hour smart city deployment

**Files:**
- `examples/smart_city.py` - PuLP implementation
- `examples/smart_city_gurobi.py` - Gurobi implementation (recommended for speed)
- `models/smart_city_data.dat` - AMPL data file (if applicable)
- `notebooks/smart_city.ipynb` - Interactive notebook with visualizations

**Run:**
```bash
python examples/smart_city.py
```

**Scenario:**
- 5 slices: eMBB, uRLLC, mMTC, PublicSafety, VideoSurveillance
- 4 links: fiber, microwave, mmWave, sub-6GHz
- 24 time slots (hourly)
- Dynamic traffic patterns
- Expected output: 33,748 Mbps total allocation

---

## 🛠️ Installation
```bash
# Install all dependencies
pip install -r requirements.txt

# For Gurobi (optional, requires license)
pip install gurobipy
```

**Dependencies:**
- `pulp>=2.7.0` - Open-source LP solver
- `gurobipy>=10.0.0` - Commercial solver (optional)
- `numpy>=1.21.0` - Numerical computing
- `matplotlib>=3.5.0` - Visualization
- `seaborn>=0.12.0` - Statistical visualization
- `jupyter>=1.0.0` - Interactive notebooks

---

## 📊 Output Examples

### Simple Demo Output
```
==================================================
5G NETWORK SLICING OPTIMIZATION
==================================================

Status: Optimal

📅 Time Slot 1:
  slice1 → link1: 50 Mbps
  slice2 → link2: 60 Mbps
  slice3 → link1: 40 Mbps, link2: 50 Mbps

💡 Total Optimized Bandwidth: 370 Mbps
==================================================
```

### Smart City Output
```
==================================================
5G SMART CITY NETWORK SLICING
==================================================

📅 Time Slot 8 (Peak Hour):
  eMBB                 → fiber: 600 Mbps, mmwave: 360 Mbps
  uRLLC                → fiber: 360 Mbps, mmwave: 240 Mbps
  mMTC                 → fiber: 36 Mbps, microwave: 24 Mbps
  ...

💡 Total Optimized Bandwidth: 33,748 Mbps
==================================================
```

---

## 🔧 AMPL Models

### Using AMPL Directly
```bash
# Simple demo
ampl models/model.mod models/simple_data.dat

# Smart City
ampl models/model.mod models/smart_city_data.dat
```

**Model Files:**
- `models/model.mod` - Mathematical formulation (shared)
- `models/simple_data.dat` - Data for simple example
- `models/smart_city_data.dat` - Data for smart city

---

## 📈 Visualization

All examples generate visualizations when run. Smart City example creates:

1. **Time series plot** - Bandwidth over 24 hours
2. **Heatmap** - Allocation patterns
3. **Link utilization chart** - Capacity vs usage
4. **Dashboard** - Combined view (saved as PNG)

**View visualizations:**
```bash
# use Jupyter notebook for interactive plots
jupyter notebook notebooks/smart_city.ipynb
```

---

## 🐛 Troubleshooting

### Import Error: No module named 'pulp'
```bash
pip install pulp
```

---

## 💡 Tips

1. **Start with simple demo** to understand the model
2. **Use Jupyter notebooks** for interactive exploration
3. **Try Gurobi** for faster large-scale optimization
4. **Modify data files** to test your own scenarios
5. **Check visualizations** to validate results

---

## 🤝 Contributing

To add new scenarios:

1. Create new file in `examples/your_scenario.py`
2. Define slices, links, time slots
3. Set capacity and demand data
4. Follow the same model structure
5. Add visualization code

---

