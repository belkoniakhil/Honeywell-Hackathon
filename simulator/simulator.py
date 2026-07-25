"""
simulator.py

Main simulator class.

This class coordinates the simulation.
It owns the current WellState and updates it every simulation step.
"""

from config import SimulationConfig
from simulator.state import WellState
from simulator.flow_model import FlowModel


class OilWellSimulator:

    def __init__(self, config: SimulationConfig):

        self.config = config

        self.flow_model = FlowModel(config)

        self.state = WellState(
            time=0.0,
            flow=config.initial_flow,
            whp=config.initial_whp,
            flp=config.initial_flp,
            bhp=config.initial_bhp,
            choke=config.initial_choke,
        )

    def reset(self) -> WellState:
        """
        Reset simulator to initial conditions.
        """

        self.state = WellState(
            time=0.0,
            flow=self.config.initial_flow,
            whp=self.config.initial_whp,
            flp=self.config.initial_flp,
            bhp=self.config.initial_bhp,
            choke=self.config.initial_choke,
        )

        return self.state

    def step(self, new_choke: float) -> WellState:
        """
        Advance simulation by one timestep.
        """

        new_flow = self.flow_model.next_flow(
            self.state,
            new_choke
        )

        self.state = WellState(
            time=self.state.time + self.config.time_step,
            flow=new_flow,
            whp=self.state.whp,
            flp=self.state.flp,
            bhp=self.state.bhp,
            choke=new_choke,
        )

        return self.state

    def current_state(self) -> WellState:
        """
        Return current simulator state.
        """
        return self.state