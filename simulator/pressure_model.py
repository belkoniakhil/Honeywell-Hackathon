"""
pressure_model.py

Dataset calibrated pressure model.
"""

from config import SimulationConfig
from simulator.state import WellState
from utils.data_loader import DatasetLoader


class PressureModel:

    def __init__(
        self,
        config: SimulationConfig,
        dataset: DatasetLoader,
    ):

        self.config = config
        self.dataset = dataset

    def next_pressures(
        self,
        current_state: WellState,
        new_choke: float,
    ):

        alpha = (
            self.config.time_step
            / self.config.pressure_time_constant
        )

        desired_whp = self.dataset.whp(new_choke)
        desired_flp = self.dataset.flp(new_choke)
        desired_bhp = self.dataset.bhp(new_choke)

        whp = current_state.whp + alpha * (
            desired_whp - current_state.whp
        )

        flp = current_state.flp + alpha * (
            desired_flp - current_state.flp
        )

        bhp = current_state.bhp + alpha * (
            desired_bhp - current_state.bhp
        )

        return whp, flp, bhp