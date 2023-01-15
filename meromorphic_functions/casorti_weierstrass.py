import numpy as np

# Define the region D and the point z0
D = {z: abs(z) < 1}
z0 = 2

# Define the function f(z) = (z-z0)^(-1)
f = lambda z: 1/(z-z0)

# Check if z0 is in the closure of D
if not any([z0 == x for x in D]):
    # Compute the values of f(z) for z in D
    values = [f(z) for z in D]

    # Check if the set of values is dense in the complex plane
    if len(values) == np.inf:
        print("The set of values is dense in the complex plane")
    else:
        print("The set of values is not dense in the complex plane")
else:
    print("z0 is in the closure of D")
