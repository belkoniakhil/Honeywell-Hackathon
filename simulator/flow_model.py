"""
flow_model.py
-------------

This module is responsible ONLY for calculating the oil flow.

Responsibilities
----------------
1. Estimate the desired (steady-state) flow for a given choke position.
2. Move the current flow gradually towards the desired flow.
3. Ensure the flow always remains within configured limits.

It does NOT

- modify WellState
- calculate pressures
- know anything about the controller
"""

from config import SimulationConfig
from simulator.state import WellState


class FlowModel:
    """
    Calculates oil flow dynamics.
    """

    def __init__(self, config: SimulationConfig):
        """
        Store simulator configuration.
        """
        self.config = config

    def next_flow(
        self,
        current_state: WellState,
        new_choke: float
    ) -> float:
        """
        Compute the next oil flow.

        Parameters
        ----------
        current_state : WellState
            Current physical state of the well.

        new_choke : float
            New choke position requested by the controller.

        Returns
        -------
        float
            Updated oil flow.
        """

        desired_flow = self._desired_flow(new_choke)

        updated_flow = self._dynamic_response(
            current_state.flow,
            desired_flow
        )

        return self._clamp(updated_flow)

    # ---------------------------------------------------------
    # Internal Methods
    # ---------------------------------------------------------

    def _desired_flow(self, choke: float) -> float:
        """
        Estimate steady-state flow.

        NOTE
        ----
        Temporary implementation.

        Later this will be calibrated using the Honeywell
        sample dataset.
        """

        fraction = choke / self.config.max_choke

        return (
            self.config.min_flow
            + fraction
            * (self.config.max_flow - self.config.min_flow)
        )

    def _dynamic_response(
        self,
        current_flow: float,
        desired_flow: float
    ) -> float:
        """
        First-order dynamic response.

        Instead of jumping instantly to the desired flow,
        move only a fraction of the remaining distance.
        """

        alpha = (
            self.config.time_step
            / self.config.flow_time_constant
        )

        return current_flow + alpha * (
            desired_flow - current_flow
        )

    def _clamp(
        self,
        flow: float
    ) -> float:
        """
        Keep flow inside physical limits.
        """

        return max(
            self.config.min_flow,
            min(flow, self.config.max_flow)
        )