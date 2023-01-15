import numpy as np
from sympy import *

# Define the function with a singularity at z0 = 0
z = symbols('z')
f = 1/(z-1)

# Compute the limit as z approaches 0
z0 = 0
limit = limit(f, z, z0)

# Check if the limit is finite
if limit.is_finite:
    # Redefine the function at z0 = 0
    f = f.subs(z, z+1)
    print("The singularity is removable and the function is now continuous at z0 = 0")
    print(f)
else:
    print("The singularity is not removable")
