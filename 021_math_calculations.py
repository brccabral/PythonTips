# use numpy and pandas

import numpy as np


def avoid_math_in_python():
    x = list(range(100))
    y = list(range(100))
    s = [a+b for a, b in zip(x, y)]


def use_numpy():
    x = np.arange(100)
    y = np.arange(100)
    s = x + y

# use pandas for analysis
