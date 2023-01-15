import sympy as sp

# Define the function
z = sp.Symbol('z')
f = (1/(z-1))**2

# Find the poles of the function
poles = f.poles()

# Find the essential singularities of the function
essential_singularities = f.essential_singularities()

# Check if the function is meromorphic
if len(poles) + len(essential_singularities) == 0:
    print("The function is holomorphic and thus not meromorphic")
elif len(essential_singularities) == 0:
    print("The function is meromorphic and has poles at", poles)
else:
    print("The function is meromorphic and has poles at", poles, "and essential singularities at", essential_singularities)
