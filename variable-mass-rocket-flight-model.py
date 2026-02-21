import numpy as np
import matplotlib
# use non-interactive backend to avoid GUI / shared-lib issues on headless systems
matplotlib.use('Agg')
import matplotlib.pyplot as plt

g = 9.81  # gravitational acceleration (m/s^2)

# ------------------------
# USER INPUTS
# ------------------------
v0 = float(input("Initial velocity (m/s): "))
angle_deg = float(input("Launch angle (degrees): "))
T = float(input("Thrust force (N): "))
m0 = float(input("Initial total mass (kg): "))
mfuel = float(input("Fuel mass (kg): "))
t_burn = float(input("Burn time (s): "))
t_max = float(input("Total simulation time (s): "))

# ------------------------
# INITIAL CALCULATIONS
# ------------------------
angle = np.radians(angle_deg)

vx = v0 * np.cos(angle)
vy = v0 * np.sin(angle)

dt = 0.01
time = np.arange(0, t_max + dt, dt)

# Protect against zero burn time
if t_burn <= 0 or mfuel <= 0:
    mdot = 0.0
else:
    mdot = mfuel / t_burn  # mass flow rate (kg/s)

# initial mass
m = m0

# Position
px, py = 0.0, 0.0

# Storage arrays
x = []
y = []
velocity = []
mass_history = []
time_history = []

# ------------------------
# SIMULATION LOOP
# ------------------------
for t in time:

    # Thrust active while t < t_burn and there's fuel remaining
    if t <= t_burn and m > (m0 - mfuel) and mdot > 0:
        # decrease mass but never below dry mass (m0 - mfuel)
        m = max(m - mdot * dt, m0 - mfuel)

        # thrust acceleration components along launch angle
        ax = (T / m) * np.cos(angle)
        ay = (T / m) * np.sin(angle) - g
    else:
        ax = 0.0
        ay = -g

    # Update velocities
    vx += ax * dt
    vy += ay * dt

    # Update positions
    px += vx * dt
    py += vy * dt

    # store
    x.append(px)
    y.append(py)
    velocity.append(np.sqrt(vx ** 2 + vy ** 2))
    mass_history.append(m)
    time_history.append(t)

    if py < 0:
        break

# ------------------------
# RESULTS
# ------------------------
print("\nSimulation Complete")
if len(mass_history) > 0:
    print(f"Final Mass: {mass_history[-1]:.2f} kg")
else:
    print(f"Final Mass: {m:.2f} kg")

if len(y) > 0:
    print(f"Max Height: {max(y):.2f} m")
else:
    print("Max Height: 0.00 m")

if len(x) > 0:
    print(f"Range: {x[-1]:.2f} m")
else:
    print("Range: 0.00 m")

# ------------------------
# PLOTTING
# ------------------------

# Trajectory Plot
plt.figure()
plt.plot(x, y)
plt.xlabel("Horizontal Distance (m)")
plt.ylabel("Vertical Height (m)")
plt.title("Rocket Trajectory (Variable Mass)")
plt.grid()
plt.tight_layout()
plt.savefig("trajectory.png")

# Velocity vs Time
plt.figure()
plt.plot(time_history, velocity)
plt.title("Velocity vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.tight_layout()
plt.savefig("velocity.png")

# Mass vs Time
plt.figure()
plt.plot(time_history, mass_history)
plt.title("Mass vs Time")
plt.xlabel("Time (s)")
plt.ylabel("Mass (kg)")
plt.grid()
plt.tight_layout()
plt.savefig("mass.png")

print("Plots saved: trajectory.png, velocity.png, mass.png")
print(f"Thrust-to-Weight Ratio: {T/(m0*g):.2f}")