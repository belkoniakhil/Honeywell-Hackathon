"""
validator.py

Validation utilities for simulator state.
"""

from config import SimulationConfig
from simulator.state import WellState


class Validator:

    def __init__(self, config: SimulationConfig):
        self.config = config

    # ---------------------------------------------------------

    def validate_choke(self, choke: float):

        if choke < self.config.min_choke:
            raise ValueError(
                f"Choke {choke} is below minimum limit ({self.config.min_choke})."
            )

        if choke > self.config.max_choke:
            raise ValueError(
                f"Choke {choke} is above maximum limit ({self.config.max_choke})."
            )

    # ---------------------------------------------------------

    def validate_state(self, state: WellState):

        if not (
            self.config.min_flow
            <= state.flow
            <= self.config.max_flow
        ):
            raise ValueError(
                f"Invalid Flow: {state.flow:.2f} "
                f"(Allowed: {self.config.min_flow} - {self.config.max_flow})"
            )

        if not (
            self.config.min_whp
            <= state.whp
            <= self.config.max_whp
        ):
            raise ValueError(
                f"Invalid WHP: {state.whp:.2f} "
                f"(Allowed: {self.config.min_whp} - {self.config.max_whp})"
            )

        if not (
            self.config.min_flp
            <= state.flp
            <= self.config.max_flp
        ):
            raise ValueError(
                f"Invalid FLP: {state.flp:.2f} "
                f"(Allowed: {self.config.min_flp} - {self.config.max_flp})"
            )

        if not (
            self.config.min_bhp
            <= state.bhp
            <= self.config.max_bhp
        ):
            raise ValueError(
                f"Invalid BHP: {state.bhp:.2f} "
                f"(Allowed: {self.config.min_bhp} - {self.config.max_bhp})"
            )