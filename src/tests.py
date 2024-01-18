import numpy as np
import galsim

# Given FWHM quartiles and mean for PSF distribution
q1 = 0.49
q2 = 0.62
q3 = 0.78
mean = 0.66

fwhms = np.array([0.49, 0.62, 0.66, 0.78, 0.83])
fwhms = np.linspace(fwhms[0], fwhms[-1], 100)
fwhm = np.random.choice(fwhms)
print(fwhms.mean())
print(fwhm)

def calculate_fwhm_from_distribution(initial_fwhms):
    fwhms = np.linspace(initial_fwhms[0], initial_fwhms[-1], 100)
    return np.random.choice(fwhms)
