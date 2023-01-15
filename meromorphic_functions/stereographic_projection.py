import numpy as np
import cmath

# Define the spherical coordinates of the point P
r = 2
theta = np.pi/4
phi = np.pi/3

# Define the reference point S
S = (0, 0, 1)

# Convert spherical coordinates to cartesian coordinates
x = r * np.sin(phi) * np.cos(theta)
y = r * np.sin(phi) * np.sin(theta)
z = r * np.cos(phi)

# Find the stereographic projection of P
P_prime = complex((2 * x) / (1 + z), (2 * y) / (1 + z))

print("The stereographic projection of the point P on the Riemann sphere is", P_prime)
