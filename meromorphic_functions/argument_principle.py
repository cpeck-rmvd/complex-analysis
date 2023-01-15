import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from shapely.geometry import Polygon, Point

# Define the function and the contour
z = symbols('z')
f = (z-1)*(z-2)*(z-3)/((z-4)*(z-5)*(z-6))
C = Circle((0, 0), 2)

# Find the zeros and poles of the function inside the contour
zeros = solve(f)
poles = [p for p in zeros if abs(p) > 2]

# Plot the contour and the zeros and poles
plt.figure()
plt.axes().set_aspect('equal')
plt.plot(*C.args[0], color='blue')
plt.scatter(*np.array(zeros).T, color='red')
plt.scatter(*np.array(poles).T, color='black')

# Find the total change in the argument of f(z) as one moves along C
arg_change = 0
for i in range(1001):
    z = C.args[0][0][i] + 1j*C.args[0][1][i]
    arg_change += arg(f.subs(z, z))
arg_change = arg_change/1001

# Check if the Argument Principle holds
if len(zeros) - len(poles) == arg_change/(2*np.pi):
    print("The Argument Principle holds")
else:
    print("The Argument Principle does not hold")

    
# For toy contours

# Define the function and the contour
z = symbols('z')
f = (z-1)*(z-2)*(z-3)/((z-4)*(z-5)*(z-6))

points = [(1,1), (2,2), (3,1), (2,0), (1,1)]
poly = Polygon(points)

# Find the zeros and poles of the function inside the contour
zeros = solve(f)
poles = [p for p in zeros if not poly.contains(Point(p))]

# Find the total change in the argument of f(z) as one moves along C
arg_change = 0
for point in points:
    z = point[0] + 1j*point[1]
    arg_change += arg(f.subs(z, z))
arg_change = arg_change/(len(points))

# Check if the Argument Principle holds
if len(zeros) - len(poles) == arg_change/(2*np.pi):
    print("The Argument Principle holds")
else:
    print("The Argument Principle does not hold")
