from math import sqrt
from typing import List

Vector = List[float]


def mean(v: Vector) -> float:
    """Calculates mean of vector."""
    return sum(v) / len(v)


def variance(v: Vector) -> float:
    """Calculates variance of vector."""
    return sum((v_i - mean(v)) ** 2 for v_i in v) / (len(v) - 1)


def standard_deviation(v: Vector) -> float:
    """Calculates standard deviation of vector."""
    return sqrt(variance(v))
