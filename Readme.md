# Numerical-ODE-PDE-Solvers

A comprehensive collection of Python and MATLAB scripts for solving ordinary differential equations (ODEs) and performing high-dimensional numerical integration.  
This repository is ideal for students, educators, and researchers seeking practical demonstrations and templates for classic numerical analysis techniques.

---

## 📂 Repository Structure

Numerical-ODE-PDE-Solvers-2-/
│
├── python/
│   ├── euler_logistic_adaptive.py
│   ├── rk4_linear_system.py
│   ├── implicit_midpoint_vs_euler.py
│   ├── mc_integral_multidim.py
│   └── README.md
│
├── matlab/
│   ├── euler_logistic_adaptive.m
│   ├── rk4_linear_system.m
│   ├── implicit_midpoint_vs_euler.m
│   ├── mc_integral_multidim.m
│   └── README.md
│
├── LICENSE
└── README.md  ← (this file)

---

## 🚀 What’s Included?

- **Explicit Euler Method:**  
  Fixed and adaptive step size for classic IVPs, e.g. logistic growth.
- **Runge-Kutta 4th Order (RK4):**  
  For linear ODE systems.
- **Implicit Midpoint Method:**  
  With comparison to explicit Euler, especially for stiff systems.
- **Monte Carlo Integration:**  
  For evaluating multidimensional integrals and observing the curse of dimensionality.

All code is available in **both Python and MATLAB** for easy comparison and versatility.

---

## 📖 How to Use

### Python

1. Navigate to the `python/` folder.
2. Run any script in your Python environment:
   ```bash
   python scriptname.py

(Requires numpy and matplotlib.)

### MATLAB
	1.	Navigate to the matlab/ folder.
	2.	Open and run any .m file in MATLAB or GNU Octave.

Each script is self-contained and will generate plots/results directly.

⸻

📝 Topics Demonstrated
	•	Step size control in ODE solvers
	•	Stability of explicit vs implicit methods
	•	Solving stiff ODEs
	•	High-dimensional quadrature with Monte Carlo
	•	Comparison of numerical and exact results

