import math

def tanh(n):
    """Returns the Taylor series for tanh(z) at z = 0."""
    a = []
    for i in range(n):
        a.append(2 / ((2 * i - 1) * (2 * i - 1)))
    return a

def radius_of_convergence(a):
    """Returns the radius of convergence of the Taylor series."""
    limsup = 0
    for i, a_i in enumerate(a):
        limsup = max(limsup, abs(a_i) ** (1 / i))
    return 1 / limsup

def agrees_to_n_decimal_places(x, n):
    """Returns True if the Taylor series for tanh(x) agrees with tanh(x) to n decimal places, False otherwise."""
    return math.isclose(math.tanh(x), sum(tanh(n)), rel_tol=10 ** (-n), abs_tol=0)

def find_n():
    """Returns the smallest value of N such that the Taylor series for tanh(1) agrees with tanh(1) to 1000 decimal places."""
    n = 0
    while not agrees_to_n_decimal_places(1, n):
        n += 1
    return n

def main():
    a = tanh(5)
    print("a5 =", a[4])
    r = radius_of_convergence(a)
    print("Radius of convergence:", r)
    n = find_n()
    print("N =", n)

if __name__ == "__main__":
    main()
