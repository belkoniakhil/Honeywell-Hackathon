"""
decision.py

Decision object returned by the optimizer.
"""

from dataclasses import dataclass


@dataclass
class ControlDecision:

    selected_choke: float

    predicted_flow: float

    tracking_error: float

    movement_penalty: float

    pressure_penalty: float

    total_cost: float