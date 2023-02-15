import pandas as pd
from Patient import Patient
from typing import List, Tuple
from constants import FEATURES_NO
from linear_algebra import Vector, vector_mean
from statistics import standard_deviation


def parse_data(data: pd.DataFrame) -> List[Patient]:
    elements = []
    for i in range(len(data)):
        point = [data.iloc[i][j] for j in range(2, FEATURES_NO)]
        label = data.iloc[i][1]
        elements.append(Patient(point, label))
    return elements


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    dim = len(data[0])
    means = vector_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data])
              for i in range(dim)]
    return means, stdevs


def rescale(data: List[Patient]) -> List[Patient]:
    points = [patient.point for patient in data]

    dim = len(points[0])
    means, stdevs = scale(points)

    rescaled = [v.copy() for v in points]

    for v in rescaled:
        for i in range(dim):
            if stdevs[i] > 0:
                v[i] = (v[i] - means[i]) / stdevs[i]

    rescaled_data = []
    for i in range(len(data)):
        rescaled_data.append(Patient(rescaled[i], data[i].label))

    return rescaled_data
