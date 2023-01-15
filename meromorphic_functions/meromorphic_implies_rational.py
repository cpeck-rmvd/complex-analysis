import sympy as sp

# Define a general meromorphic function
z = sp.Symbol('z')
f = sp.Function('f')(z)

# Find the poles and essential singularities
poles = f.poles()
essential_singularities = f.essential_singularities()

# Create the numerator and denominator polynomials
numerator = 1
denominator = 1

# Multiply the numerator and denominator by (z-p) for each pole p
for pole in poles:
    numerator *= (z-pole[0])
    denominator *= (z-pole[0])

# Multiply the numerator by (z-s)^m for each essential singularity s and its multiplicity m
for essential_singularity in essential_singularities:
    numerator *= (z-essential_singularity[0])**essential_singularity[1]

# Express the function as the ratio of the polynomials
f_new = numerator/denominator
print(f_new)
