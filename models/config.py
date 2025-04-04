from dataclasses import dataclass
import numpy as np


@dataclass
class DroneXZConfig:
    nx: int = 6
    nu: int = 2
    mass: float = 1.0
    l: float = 0.5

@dataclass
class BicycleXYConfig:
    nx: int = 3
    nu: int = 2
    lf: float = 0.5
    lr: float = 0.5
    safety_radius: float = 0.8