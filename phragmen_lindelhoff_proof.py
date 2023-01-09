import numpy as np
from scipy.optimize import linprog

# Define the function f(z) = exp(z)
def f(z):
    return np.exp(z)

# Define the boundary of the region D in the complex plane
r = 1 # radius of the circle
theta = np.linspace(0, 2*np.pi, 100) # angles of the points on the circle
x = r * np.cos(theta) # real parts of the points
y = r * np.sin(theta) # imaginary parts of the points

# Compute the maximum modulus of f(z) on the boundary of D
modulus = np.abs(f(x + 1j*y)) # modulus of f(z) at each point on the boundary
max_modulus = np.max(modulus) # maximum modulus

# Use linear programming to find the point on the boundary where the maximum modulus is achieved
c = -1 # objective function coefficient
A_ub = np.vstack([x, y]) # inequality constraints
b_ub = r * np.ones(len(x)) # inequality constraints
x0_bounds = (0, None) # bounds on the real part of z
y0_bounds = (0, None) # bounds on the imaginary part of z
res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=[x0_bounds, y0_bounds])

# Print the result
print(f"The maximum modulus of f(z) on the boundary of D is {max_modulus:.4f}")
print(f"The point on the boundary where the maximum modulus is achieved is {res.x[0]:.4f} + {res.x[1]:.4f}j")
