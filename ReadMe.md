# 🚀 Aerospace Simulation & Dynamics Lab

## Overview

This repository contains aerospace-focused numerical simulations developed to study flight dynamics, propulsion behavior, and launch vehicle performance using first-principles physics and computational methods.

The objective is to build practical, simulation-driven engineering intuition for aerospace systems through numerical modeling and analysis.

---

## Current Modules

### Launch Vehicle Ascent Dynamics

A 2D numerical simulation of rocket ascent including:

- Variable mass modeling (propellant depletion)
- Thrust vector decomposition
- Boost and coast phase simulation
- Thrust-to-weight ratio evaluation
- Time-stepped numerical integration
- Ground-impact termination logic
- Trajectory, velocity, mass, and acceleration visualization

---

## Physics Model

The ascent simulation is based on Newton’s Second Law:

F = m(t) a

---

### Powered Flight (Thrust Phase)

Acceleration components:

a_x = (T / m(t)) * cos(theta)  
a_y = (T / m(t)) * sin(theta) - g  

Where:

- T = thrust force  
- m(t) = instantaneous mass  
- theta = launch angle  
- g = gravitational acceleration  

---

### Mass Variation During Burn

m(t) = m0 - m_dot * t  

Where:

- m0 = initial total mass  
- m_dot = mass flow rate (m_dot = m_fuel / t_burn)  

---

### Coast Phase (After Burnout)

a_x = 0  
a_y = -g  

---

## Assumptions

- No aerodynamic drag (baseline model)
- Constant thrust magnitude during burn
- Constant thrust direction
- Flat Earth approximation
- No atmospheric variation

---

## Outputs

The simulator generates:

- Trajectory (x–y)
- Velocity vs time
- Mass vs time
- Acceleration vs time
- Thrust-to-weight ratio evaluation

These outputs enable basic ascent performance characterization.

---

## Future Work

Planned extensions include:

- Aerodynamic drag modeling
- Variable thrust profiles
- Thrust vector control
- Multi-stage vehicle modeling
- Orbital insertion simulations
- Guidance and control algorithms

---

## Tech Stack

- Python
- NumPy
- Matplotlib

---

## Author

Jagadeesh  
Aerospace Engineer  
Focused on propulsion modeling, flight dynamics, and simulation-based analysis.
