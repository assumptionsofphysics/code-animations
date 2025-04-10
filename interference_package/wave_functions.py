from ._imports import *
from .constants import a, b, k, c1, z
from .helpers import R

# Define psi1 function
def psi1(x, d):
    real_integrand = lambda ys, xs: k / (2 * np.pi) * (1 / np.sqrt(2 * a * b)) * \
        np.real(np.exp(1j * (k * R(x, xs, ys) + np.pi/2))) / R(x, xs, ys) * (z / R(x, xs, ys))

    imag_integrand = lambda ys, xs: k / (2 * np.pi) * (1 / np.sqrt(2 * a * b)) * \
        np.imag(np.exp(1j * (k * R(x, xs, ys) + np.pi/2))) / R(x, xs, ys) * (z / R(x, xs, ys))

    real_result, real_error = integrate.dblquad(real_integrand, d/2 - a/2, d/2 + a/2, -b/2, b/2)
    imag_result, imag_error = integrate.dblquad(imag_integrand, d/2 - a/2, d/2 + a/2, -b/2, b/2)

    return real_result + 1j * imag_result


# Define psi2 function
def psi2(x, d):
    real_integrand = lambda ys, xs: k / (2 * np.pi) * (1 / np.sqrt(2 * a * b)) * \
        np.real(np.exp(1j * (k * R(x, xs, ys) + np.pi/2))) / R(x, xs, ys) * (z / R(x, xs, ys))

    imag_integrand = lambda ys, xs: k / (2 * np.pi) * (1 / np.sqrt(2 * a * b)) * \
        np.imag(np.exp(1j * (k * R(x, xs, ys) + np.pi/2))) / R(x, xs, ys) * (z / R(x, xs, ys))

    real_result, real_error = integrate.dblquad(real_integrand, -d/2 - a/2, -d/2 + a/2, -b/2, b/2)
    imag_result, imag_error = integrate.dblquad(imag_integrand, -d/2 - a/2, -d/2 + a/2, -b/2, b/2)

    return real_result + 1j * imag_result


# Define intensity functions I1, I2, and Is
def I1(x, d, c1=c1):
    return abs(c1 * psi1(x, d))**2


def I2(x, d, c1=c1):
    c2_local = np.sqrt(1 - abs(c1)**2)
    return abs(c2_local * psi2(x, d))**2


def psi(x, d, c1=c1):
    c2_local = np.sqrt(1 - abs(c1)**2)
    return c1 * psi1(x, d) + c2_local * psi2(x, d)


def Is(x, d, c1=c1):
    return abs(psi(x, d, c1))**2


def spherical_path(t):
  theta = t * np.pi/2  # Latitude angle
  phi = 0.5 * np.pi  # Longitude angle
  x = 2 * np.sin(phi) * np.cos(theta)
  y = 2 * np.sin(phi) * np.sin(theta)
  z = 2 * np.cos(phi)
  return np.array([x, y, z])

def find_c1(pos):
  theta = np.arctan2(pos[1], pos[0])
  phi = np.arccos(pos[2] / np.linalg.norm(pos))
  c1 = np.exp(1j*theta)*np.sin(phi/2)
  return c1