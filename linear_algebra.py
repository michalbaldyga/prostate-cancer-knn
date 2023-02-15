from typing import List
import math

Vector = List[float]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Calculates vectors means."""
    return [sum(vector[i] for vector in vectors) / len(vectors) for i in range(len(vectors[0]))]


def sum_of_squares(v: Vector) -> float:
    """v_1 * v_1 + ... + v_n * v_n"""
    return sum([v_i ** 2 for v_i in v])
