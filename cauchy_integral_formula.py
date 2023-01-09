def cauchy_integral_formula(f, z, r):
    def g(t):
        return f(z + r * math.exp(1j * t)) * math.exp(-1j * t)
    return 1j / (2 * math.pi) * scipy.integrate.quad(g, 0, 2 * math.pi)[0]

def test_cauchy_integral_formula(f, r):
    def g(t):
        return f(r * math.exp(1j * t))
    integral = 1j / (2 * math.pi) * scipy.integrate.quad(g, 0, 2 * math.pi)[0]
    cauchy = cauchy_integral_formula(f, 0, r)
    return math.isclose(integral, cauchy, rel_tol=1e-6, abs_tol=1e-6)

def main():
    def f1(z):
        return 1 / z
    print(test_cauchy_integral_formula(f1, 1))
    print(test_cauchy_integral_formula(f1, 2))

    def f2(z):
        return z ** 2
    print(test_cauchy_integral_formula(f2, 1))
    print(test_cauchy_integral_formula(f2, 2))

if __name__ == "__main__":
    main()
