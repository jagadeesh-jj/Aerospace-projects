import math

# Constants
R = 287       # J/kg-K (adjust for propellant if needed)
g0 = 9.81     # m/s^2

def area_mach_relation(M, gamma):
    term1 = (2 / (gamma + 1))
    term2 = (1 + (gamma - 1)/2 * M**2)
    exponent = (gamma + 1) / (2 * (gamma - 1))
    return (1/M) * (term1 * term2) ** exponent

def solve_exit_mach(area_ratio, gamma):
    M = 2.0  # Initial guess (supersonic)
    for _ in range(1000):
        f = area_mach_relation(M, gamma) - area_ratio
        df = (area_mach_relation(M + 1e-6, gamma) - area_mach_relation(M - 1e-6, gamma)) / 2e-6
        M = M - f/df
    return M

def mass_flow_rate(Pc, At, gamma, Tc):
    return (Pc * At / math.sqrt(Tc)) * \
           math.sqrt(gamma / R) * \
           ( (2 / (gamma + 1)) ** ((gamma + 1)/(2*(gamma - 1))) )

def exit_conditions(Tc, Pc, gamma, Me):
    Te = Tc / (1 + (gamma - 1)/2 * Me**2)
    Pe = Pc * (Te / Tc) ** (gamma/(gamma - 1))
    Ve = Me * math.sqrt(gamma * R * Te)
    return Te, Pe, Ve

if __name__ == "__main__":
    print("=== Isentropic Nozzle Performance Model ===\n")

    Pc = float(input("Chamber Pressure (Pa): "))
    Tc = float(input("Chamber Temperature (K): "))
    gamma = float(input("Specific Heat Ratio (gamma): "))
    At = float(input("Throat Area (m^2): "))
    Ae = float(input("Exit Area (m^2): "))
    Pa = float(input("Ambient Pressure (Pa): "))

    area_ratio = Ae / At
    Me = solve_exit_mach(area_ratio, gamma)

    mdot = mass_flow_rate(Pc, At, gamma, Tc)
    Te, Pe, Ve = exit_conditions(Tc, Pc, gamma, Me)

    thrust = mdot * Ve + (Pe - Pa) * Ae
    Isp = thrust / (mdot * g0)

    print("\n--- Results ---")
    print(f"Exit Mach: {Me:.3f}")
    print(f"Exit Velocity: {Ve:.2f} m/s")
    print(f"Mass Flow Rate: {mdot:.3f} kg/s")
    print(f"Exit Pressure: {Pe:.2f} Pa")
    print(f"Thrust: {thrust:.2f} N")
    print(f"Specific Impulse: {Isp:.2f} s")