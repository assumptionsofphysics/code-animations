from ._imports import *
from .constants import y, z, zs

# Define R as a function of x and xs, ys
def R(x, xs, ys):
    return np.sqrt((x - xs)**2 + (y - ys)**2 + (z - zs)**2)

