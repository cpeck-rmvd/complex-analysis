import math
import numpy as np
import matplotlib.pyplot as plt

def wave_function(x, t):
    """Returns the value of the wave function at the position x and time t."""
    return math.cos(x - t)

def fourier_transform(wave_function, x_min, x_max, num_samples):
    """Computes the Fourier transform of the wave function using the DFT."""
    # Create an array of x values
    x = np.linspace(x_min, x_max, num_samples)

    # Compute the DFT of the wave function
    transform = np.fft.fft(wave_function(x, 0))

    return transform

def plot_wave_function_and_fourier_transform(wave_function, x_min, x_max, num_samples):
    """Plots the wave function and its Fourier transform."""
    # Create an array of x values
    x = np.linspace(x_min, x_max, num_samples)

    # Compute the Fourier transform of the wave function
    transform = fourier_transform(wave_function, x_min, x_max, num_samples)

    # Plot the wave function and its Fourier transform
    plt.plot(x, wave_function(x, 0))
    plt.plot(x, np.abs(transform))
    plt.show()

def main():
    # Plot the wave function and its Fourier transform
    plot_wave_function_and_fourier_transform(wave_function, -10, 10, 100)

if __name__ == '__main__':
    main()
