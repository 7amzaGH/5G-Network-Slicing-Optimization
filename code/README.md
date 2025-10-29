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
```
## Files Overview

- **`dynamic_lp.py`**: Main Python implementation using PuLP
- **`model.mod`**: AMPL model definition
- **`data.dat`**: AMPL data file
- **`solver_example.ipynb`**: Interactive Jupyter notebook

## Running the Code

### Option 1: Python (PuLP)
```bash
python dynamic_lp.py
```

### Option 2: AMPL
```bash
ampl model.mod data.dat
```

### Option 3: Jupyter Notebook
```bash
jupyter notebook solver_example.ipynb
```

## Model Parameters

- **Slices**: 3 network slices (slice1, slice2, slice3)
- **Links**: 2 physical links (link1, link2)
- **Time Slots**: 2 time periods
- **Capacity**: link1=100 Mbps, link2=120 Mbps

## Output

The model outputs the optimal bandwidth allocation for each slice across links and time slots.
