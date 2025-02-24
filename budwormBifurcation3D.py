import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  

# By default, we are using the budworm logistic population model which has been adjusted to account for predation by birds
# If you'd like to use another two-parameter ODE, define a population range of values that represent potential equilibria, and plug in your equation for the two parmameters you wish to generate a three dimensional bifurcation diagram for

p = np.linspace(1.001,5,500)

r= 2*p**3 / (1+ p**2)**2
N= 2*p**3 / (p**2-1)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot(N, r, p, lw=2, label='Bifurcation curve')
ax.set_xlabel('Carrying Capacity N')
ax.set_ylabel('Growth Rate r')
ax.set_zlabel('Equilibrium Population P')
ax.set_title('3D Bifurcation Diagram for Budworm Model')
ax.legend()

plt.tight_layout()
plt.savefig("budworm_bifurcation_3d.png")
plt.show()