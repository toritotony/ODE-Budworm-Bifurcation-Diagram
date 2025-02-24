import numpy as np
import matplotlib.pyplot as plt

# By default, we use the adjust budworm logistic population model
# If you'd like to use your own one parameter ODE or focus on one paramater in a multi-parameter ODE, just replace r with the desired param

P = np.linspace(1.001, 5, 500)
r = 2 * P**3 / (1 + P**2)**2

plt.figure(figsize=(8, 6))
plt.plot(r, P, 'r-', label='Nonzero equilibria (P>1)')
plt.axhline(0, color='k', linestyle='--', label='Trivial equilibrium P=0')
plt.xlabel('Growth rate (r)')
plt.ylabel('Equilibrium population (P)')
plt.title('Bifurcation Diagram for the Budworm Model')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("budworm_bifurcation_2d.png", dpi=300)
plt.show()