from typing import List
from statistics import standard_deviation
from math import sqrt

Vector = List[float]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Calculates vectors means."""
    return [sum(vector[i] for vector in vectors) / len(vectors) for i in range(len(vectors[0]))]


def sum_of_squares(v: Vector) -> float:
    """v_1 * v_1 + ... + v_n * v_n"""
    return sum([v_i ** 2 for v_i in v])


def vector_stdev(vectors: List[Vector]) -> Vector:
    """Calculates vectors stdevs."""
    return [standard_deviation([vector[i] for vector in vectors]) for i in range(len(vectors[0]))]


def distance(v: Vector, u: Vector) -> float:
    """Calculates euclidean distance between vectors."""
    return sqrt(sum([(v[i] - u[i]) ** 2 for i in range(len(v))]))
