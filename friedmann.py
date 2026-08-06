#1) importing libraries

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

#2) conversion of units for hubble

# Hubble constant now
H0_km_s_Mpc = 70.0  # Hubble constant in km/s/Mpc

#in SI units (s^-1)
H0_per_s = H0_km_s_Mpc / (3.086e19)  # Hubble constant in s^-1

#in Gyr^-1
H0_per_Gyr = H0_per_s * (3.154e16)  # Hubble constant in Gyr^-1

#3) defining density parameters

Omega_m0 = 0.315      # Matter
Omega_r0 = 9.2e-5     # Radiation
Omega_L0 = 0.685      # Dark Energy
Omega_k0 = 1.0 - (Omega_m0 + Omega_r0 + Omega_L0)

#4) defining the Friedmann equation

def friedmann_equation(t, a, H0):

    a = float(np.atleast_1d(a)[0])

    if a <= 0:
        return 0

    radiation = Omega_r0 / a**4
    matter = Omega_m0 / a**3
    curvature = Omega_k0 / a**2
    dark_energy = Omega_L0

    H_squared = H0**2 * (
        radiation +
        matter +
        curvature +
        dark_energy
    )

    return a * np.sqrt(H_squared)

#5) computing age of universe

a_start = 1e-5  #(just a proxy of 0)
a_today = 1.0


def dt_da(a, t, H0):

    dadt = friedmann_equation(t, a, H0)

    if dadt <= 0: #(should mean before/ at the big bang)
        return 0  

    return 1.0 / dadt


age_solution = solve_ivp(
    fun=lambda a, t: dt_da(a, t, H0_per_Gyr),
    t_span=(a_start, a_today),
    y0=[0],
    t_eval=np.linspace(a_start, a_today, 500)
)

age_of_universe = age_solution.y[0][-1]

print(f"Age of Universe = {age_of_universe:.2f} Gyr")


#6) "a" for different universes

time = np.linspace(0, 30, 1000)

def solve_universe(Omega_m, Omega_L, Omega_r):

    global Omega_m0, Omega_L0, Omega_r0, Omega_k0

    Omega_m0 = Omega_m
    Omega_L0 = Omega_L
    Omega_r0 = Omega_r
    Omega_k0 = 1.0 - (Omega_m0 + Omega_r0 + Omega_L0)

    solution = solve_ivp(
        fun=lambda t, a: friedmann_equation(t, a, H0_per_Gyr),
        t_span=(0, 30),
        y0=[1e-5],
        t_eval=time
    )

    return solution.t, solution.y[0]


# Benchmark (Our Universe)
t_LCDM, a_LCDM = solve_universe(0.315, 0.685, 0)

# Matter-only Universe
t_M, a_M = solve_universe(1.0, 0.0, 0.0)

# Empty (Milne) Universe
t_E, a_E = solve_universe(0.0, 0.0, 0.0)

#7) plotting the results

plt.figure(figsize=(10,6))

plt.plot(
    t_LCDM,
    a_LCDM,
    lw=2,
    label="Our Universe ($\\Omega_m=0.315$, $\\Omega_\\Lambda=0.685$)"
)

plt.plot(
    t_M,
    a_M,
    '--',
    lw=2,
    label="Matter-only Universe"
)

plt.plot(
    t_E,
    a_E,
    ':',
    lw=2,
    label="Empty Universe"
)

plt.axhline(
    1,
    color='gray',
    linestyle='--',
    alpha=0.6,
    label='Today ($a=1$)'
)

plt.axvline(
    age_of_universe,
    color='blue',
    linestyle='-.',
    alpha=0.7,
    label=f'Age = {age_of_universe:.2f} Gyr'
)

plt.xlim(0,30)
plt.ylim(0,2.5)

plt.xlabel("Cosmic Time (Gyr)")
plt.ylabel("Scale Factor  a(t)")
plt.title("Evolution of the Cosmic Scale Factor")

plt.grid(alpha=0.3)
plt.legend()

plt.show()


