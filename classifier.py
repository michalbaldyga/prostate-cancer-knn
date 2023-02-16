from linear_algebra import Vector, distance
from typing import List
from Patient import Patient
from statistics import mode


def knn(k: int, train_set: List[Patient], new_point: Vector) -> str:
    """k-nearest neighbor classifier"""
    sorted_set = sorted(train_set, key=lambda tp: distance(tp.point, new_point))
    labels = [patient.label for patient in sorted_set[:k]]
    return mode(labels)
