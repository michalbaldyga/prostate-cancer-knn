from typing import NamedTuple
from linear_algebra import Vector


class Patient(NamedTuple):
    point: Vector
    label: str
