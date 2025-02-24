# ODE-Budworm-Bifurcation-Diagram
A repository that allows you to generate two bifurcation diagrams (2D and 3D versions) of the budworm population model, which is an adjusted version of the logistic population model. More information below which describes how we arrive at the equations that describe the bifurcation values in terms of the growth rate and maximum capacity. Keep in mind that we start by expressing our desire to search for equilibrium values by setting our ODE to zero.

Consider the budworm model given by

$$
\frac{dP}{dt} = rP\left(1-\frac{P}{N}\right) - \frac{P^2}{1+P^2},
$$

where \(r\) is the intrinsic growth rate and \(N\) is the carrying capacity.

### 1. Finding the Equilibria

To find the equilibria, we set dP/dt = 0. For P > 0 (ignoring the trivial equilibrium P=0, we can divide by P to obtain:
 
$$
r\left(1-\frac{P}{N}\right) = \frac{P}{1+P^2}.
$$

### 2. Bifurcation Condition

This bifurcation (known as a saddle node bifurcation) occurs when the two equilibria merge into one. In addition to the equilibrium condition, we require that the derivative with respect to P is zero:

$$
\frac{d}{dP}\left[r\left(1-\frac{P}{N}\right)-\frac{P}{1+P^2}\right] = 0.
$$

Once you set up the system and solve for both r and then N, it shows that these following conditions lead to the parametric relations with P > 1 to ensure N>0:

$$
N = \frac{2P^3}{P^2-1}, \quad \text{and} \quad r = \frac{2P^3}{(1+P^2)^2}.
$$

### 3. Interpretation

Notice that as N becomes very large, the expression for N

$$
N = \frac{2P^3}{P^2-1}
$$

forces P to be very close to 1 since for P to equal 1, N needs to approach infinity. Substituting (P at a value almost equal to 1) into the formula for r gives:

$$
r \approx \frac{2\cdot1^3}{(1+1)^2} = \frac{2}{4} = 0.5.
$$

Thus, in the limit of a large carrying capacity, the bifurcation occurs at r approx 0.5.

---
