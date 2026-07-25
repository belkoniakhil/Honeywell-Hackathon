"""
flow_model.py

Dataset calibrated flow model.
"""

from config import SimulationConfig
from simulator.state import WellState
from utils.data_loader import DatasetLoader


class FlowModel:

    def __init__(
        self,
        config: SimulationConfig,
        dataset: DatasetLoader,
    ):

        self.config = config
        self.dataset = dataset

    def next_flow(
        self,
        current_state: WellState,
        new_choke: float,
    ) -> float:

        desired_flow = self.dataset.flow(new_choke)

        alpha = (
            self.config.time_step
            / self.config.flow_time_constant
        )

        flow = current_state.flow + alpha * (
            desired_flow - current_state.flow
        )

        return max(
            self.config.min_flow,
            min(flow, self.config.max_flow),
        )