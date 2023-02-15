from linear_algebra import Vector
from math import sqrt


def mean(v: Vector) -> float:
    return sum(v) / len(v)


def variance(v: Vector) -> float:
    return sum((v_i - mean(v)) ** 2 for v_i in v) / (len(v) - 1)


def standard_deviation(v: Vector) -> float:
    return sqrt(variance(v))
