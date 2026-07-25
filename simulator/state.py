"""
state.py
---------

This module defines the WellState class.

WellState represents the complete physical state of the oil well
at a single instant in time.

It contains ONLY runtime process variables.

No equations.
No controller logic.
No simulator logic.

Every simulation step updates one WellState object.
"""

from dataclasses import dataclass


@dataclass
class WellState:
    """
    Represents the current state of the well.
    """

    # Simulation time (seconds)
    time: float

    # Current oil production rate
    flow: float

    # Wellhead Pressure
    whp: float

    # Flowline Pressure
    flp: float

    # Bottom Hole Pressure
    bhp: float

    # Current choke opening (0 - 100 %)
    choke: float