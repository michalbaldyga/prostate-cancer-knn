import pandas as pd
from Patient import Patient
from typing import List, Tuple
from constants import FEATURES_NO
from linear_algebra import Vector, vector_mean, vector_stdev


def parse_data(data: pd.DataFrame) -> List[Patient]:
    """Converts raw data to format: List[Patient]"""
    elements = []
    for i in range(len(data)):
        point = [data.iloc[i][j] for j in range(2, FEATURES_NO)]
        label = data.iloc[i][1]
        elements.append(Patient(point, label))
    return elements


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    """Returns means and standard deviations of each column."""
    return vector_mean(data), vector_stdev(data)


def rescale(data: List[Patient]) -> List[Patient]:
    """Rescales the input so that each column has a mean of 0 and a standard deviation of 1."""

    # Extracting points from list of patients
    points = [patient.point for patient in data]

    # Making copy of each vector
    rescaled = [v.copy() for v in points]

    # Rescaling if necessary
    means, stdevs = scale(points)
    for v in rescaled:
        for i in range(len(points[0])):
            if stdevs[i] > 0:
                v[i] = (v[i] - means[i]) / stdevs[i]

    # Joining points with labels
    rescaled_data = [Patient(rescaled[i], data[i].label) for i in range(len(data))]

    return rescaled_data
