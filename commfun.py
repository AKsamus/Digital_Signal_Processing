"""Common functions used in multiple places."""

import math


def si(x):
    if x == 0:
        return 1
    return math.sin(x) / x
