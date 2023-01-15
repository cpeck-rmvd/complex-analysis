import numpy as np
import matplotlib.pyplot as plt
from sympy import *

# Define the function and the region
z = symbols('z')
f = (z-1)*(z-2)*(z-3)/((z-4)*(z-5)*(z-6))
D = Circle((0, 0), 2)

# Find the maximum of the modulus of the function inside the region
mod_values = [abs(f.subs(z, x+1j*y)) for x,y in zip(D.args[0][0],D.args[0][1])]
max_mod = max(mod_values)

# Find the maximum of the modulus of the function on the boundary of the region
boundary_values = [abs(f.subs(z, x + 1j*y)) for x, y in zip(D.args[0][0], D.args[0][1])]
boundary_max_mod = max(boundary_values)

plt.figure()
plt.axes().set_aspect('equal')
plt.plot(*D.args[0], color='blue')
plt.scatter(*np.array(D.args[0]).T, c=mod_values, cmap='Reds')


if max_mod == boundary_max_mod:
    print("The Maximum Modulus Principle holds")
else:
    print("The Maximum Modulus Principle does not hold")

