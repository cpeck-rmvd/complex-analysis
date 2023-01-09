import numpy as np
import matplotlib.pyplot as plt

# Define a function that maps the complex plane to the unit disk
def map_to_unit_disk(z):
  return (1 - np.abs(z)) / (1 + np.abs(z))

# Define a function that maps the complex plane to the upper half-plane
def map_to_upper_half_plane(z):
  return z.real + 1j * np.abs(z.imag)

# Define a function that maps the unit disk to the complex plane
def map_from_unit_disk(w):
  return (w + 1) / (1 - w)

# Define a function that maps the upper half-plane to the complex plane
def map_from_upper_half_plane(w):
  return w.real - 1j * np.abs(w.imag)

# Define a function that plots a conformal map
def plot_conformal_map(f, g, z_range=4, w_range=4, n=1000):
  # Generate a grid of complex numbers
  reals = np.linspace(-z_range, z_range, n)
  imags = np.linspace(-z_range, z_range, n)
  zs = np.array([complex(r, i) for i in imags for r in reals])

  # Apply the conformal map
  ws = f(zs)

  # Generate a grid of complex numbers in the target domain
  reals = np.linspace(-w_range, w_range, n)
  imags = np.linspace(-w_range, w_range, n)
  targets = np.array([complex(r, i) for i in imags for r in reals])

  # Apply the inverse conformal map
  z_targets = g(targets)

  # Plot the results
  plt.scatter(zs.real, zs.imag, c=ws.real, cmap="Reds")
  plt.scatter(targets.real, targets.imag, c=z_targets.real, cmap="Blues")
  plt.show()

# Test the conformal maps
plot_conformal_map(map_to_unit_disk, map_from_unit_disk)
plot_conformal_map(map_to_upper_half_plane, map_from_upper_half_plane)
