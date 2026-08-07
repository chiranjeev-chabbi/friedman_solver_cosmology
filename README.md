# Numerical visualisation of history of universe's expansion
### *numerical solutions of the Friedmann equations*


## The Beginning.

Imagine observing a distant galaxy through a telescope.

Its light is shifted towards the red end of the electromagnetic spectrum.

Measure an even distant galaxy, and the shift is even larger.

Repeat this for thousands of galaxies, and a deducable pattern appears.

The farther away a galaxy is, the faster it appears to recede.

This empirical relationship, discovered by **Edwin Hubble** in 1929, is known as **Hubble's Law**,

$$
v = H_0 d,
$$

where

- $v$ is the recession velocity,
- $d$ is the distance to the galaxy,
- $H_0$ is the present-day Hubble constant.

the equation in itself seems surprisingly simple.

Yet it raises one of the deepest questions in physics:

**Why the galaxies move apart in the first place?**

The answer is surprising.

**Galaxies are not flying through space.**

**Space itself is expanding.**

---

# The Cosmic Scale Factor

To describe an expanding Universe, cosmologists introduce a dimensionless quantity called the **scale factor**, denoted by

$$
a(t).
$$

Rather than tracking every individual galaxy, the scale factor measures how the entire fabric of space changes with time.

If two galaxies are separated by a distance

$$
D_0
$$

today,

their separation at any earlier or later time is

$$
D(t)=a(t)D_0.
$$

This function, completely describes the expansion history of the Universe.

Our objective is therefore:

**Find the function $a(t)$.**

---

# Einstein's approach

The expansion of the Universe cannot be explained using Newtonian gravity alone.

Instead, it follows from **Einstein's General Theory of Relativity**.

Applying Einstein's field equations to a homogeneous and isotropic Universe leads to the **Friedmann Equation**,

$$\left(\frac{\dot{a}}{a}\right)^2 = H_0^2 \left( \frac{\Omega_r}{a^4} + \frac{\Omega_m}{a^3} + \frac{\Omega_k}{a^2} + \Omega_\Lambda \right).$$

Symbolising the physical factors contributing to expansion of the universe.

The observable entities:

- the Big Bang
- the Cosmic Microwave Background
- galaxy formation
- accelerated cosmic expansion

is described by it.

---

# What is the Universe Made Of?

The Friedmann equation depends on the relative abundance of the different constituents of the Universe.

Each component contributes differently as the Universe expands.

| Component | Density Parameter | Evolution |
|-----------|-------------------|-----------|
| Radiation | $\Omega_r$ | $\propto a^{-4}$ |
| Matter | $\Omega_m$ | $\propto a^{-3}$ |
| Curvature | $\Omega_k$ | $\propto a^{-2}$ |
| Dark Energy | $\Omega_\Lambda$ | Constant |

These density parameters are defined relative to the **critical density**

$\rho_c$
=
$$
\frac{3H_0^2}{8\pi G},
$$

which is the density required for a spatially flat Universe.

They satisfy

$\Omega_i$
=
$$
\frac{\rho_i}{\rho_c},
$$

and

$$
\Omega_r+\Omega_m+\Omega_k+\Omega_\Lambda=1.
$$

---

# The Hubble Constant

Throughout this project we use

$H_0$
=
70
\;
\mathrm{km\,s^{-1}\,Mpc^{-1}}.
$$

For numerical integration, this quantity is converted

from
- $\mathrm{s^{-1}}$

to
- $\mathrm{Gyr^{-1}}$

so that cosmic time is measured directly in billions of years.

---

# The math to Python

The Friedmann equation here is not solved analytically.

Instead, it is rewritten as

$$
\frac{da}{dt}
=
aH(a),
$$

which is a first-order ordinary differential equation.

This equation is then integrated numerically using **SciPy's `solve_ivp`**, an adaptive **Runge Kutta** solver.

---

# Why Runge Kutta Instead of Euler?

The simplest numerical method for solving an ordinary differential equation is the **Euler Method**,

$$
y_{n+1}
=
y_n
+
hf(t_n,y_n),
$$

where the slope is estimated only once per step.

Although straightforward, Euler's method accumulates significant numerical error and becomes inaccurate for long integrations.

Runge–Kutta methods improve upon this idea by estimating the slope multiple times within each step and combining these estimates to produce a much more accurate solution.

SciPy's `solve_ivp` employs a Runge Kutta algorithm that automatically adjusts the step size according to the local error, making it both accurate and computationally efficient.

---

# Cosmological Models

This notebook explores three different Universes.

### ΛCDM Universe

The observed Universe,

$$
\Omega_m=0.315,\qquad
\Omega_\Lambda=0.685.
$$

Dark energy eventually dominates, leading to accelerated expansion.

---

### Matter Dominated Universe

$$
\Omega_m=1.
$$

Gravity continually slows the expansion.

---

### Empty (Milne) Universe

$$
\Omega_k=1.
$$

No matter.

No dark energy.

Expansion proceeds almost linearly with time.

---

# What This Project Does

- Gives first principle derivation of the Friedmann equation 
- Converts cosmological equations into Python
- Computes the age of the Universe
- Solves the expansion history numerically
- Compares multiple cosmological models
- Produces publication-quality visualizations
- Connects every mathematical equation directly to the corresponding code

---
