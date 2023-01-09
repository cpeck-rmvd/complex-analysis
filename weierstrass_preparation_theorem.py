import numpy as np

def rouche(f, g, z, r):
    def count_zeros(h):
        # Discretize the circle C(z, r) using evenly spaced points
        t = np.linspace(0, 2 * np.pi, 1000, endpoint=False)
        w = z + r * np.exp(1j * t)
        # Count the number of sign changes in the imaginary part of h(w)
        return sum(np.diff(np.sign(h(w).imag)))
    return count_zeros(f) == count_zeros(g)

  def test_rouche(f, g, r):
    return rouche(f, g, 0, r)
