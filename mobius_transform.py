import sympy

def g(z):
    """Returns the value of the rational map g(z)."""
    return (z + 1) / (z - 1)

def f(z, a, b, c, d):
    """Returns the value of the Mobius transformation f(z)."""
    return (a * z + b) / (c * z + d)

def count_solutions(a, b, c, d):
    """Returns the number of rational maps g(z) such that g(g(g(g(g(z))))) = f(z)."""
    z = sympy.Symbol('z')
    f_z = f(z, a, b, c, d)
    g_z = g(z)
    num_solutions = len(sympy.solve(g(g(g(g(g(z))))), z))
    if num_solutions == 1:
        return 1
    elif num_solutions == 5:
        return 5
    else:
        return float('inf')

def main():
    a, b, c, d = 1, 2, 3, 4
    num_solutions = count_solutions(a, b, c, d)
    print(f"Number of solutions: {num_solutions}")

if __name__ == '__main__':
    main()
