import cmath

def f(z):
    return 1/(z**2 + 1)

a = 1
b = 1

residue = (1/(2j*cmath.pi)) * (cmath.lim(f(z), z=a))

print(residue)
