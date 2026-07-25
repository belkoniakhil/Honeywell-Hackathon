"""
simulator.py

Main Oil Well Simulator.

Responsibilities
----------------
1. Maintain the current WellState.
2. Coordinate the FlowModel.
3. Coordinate the PressureModel.
4. Validate all simulator inputs and outputs.
5. Advance the simulation one timestep.

This class contains NO mathematical equations.
All physics belongs inside FlowModel and PressureModel.
"""

from config import SimulationConfig
from simulator.state import WellState
from simulator.flow_model import FlowModel
from simulator.pressure_model import PressureModel
from simulator.validator import Validator
from utils.data_loader import DatasetLoader
from simulator.history import SimulationHistory


class OilWellSimulator:
    """
    Coordinates the complete oil well simulation.
    """

    def __init__(self, config: SimulationConfig):

        self.config = config

        # Load calibration dataset
        self.dataset = DatasetLoader("data/well_data.csv")

        # Initialize models
        self.flow_model = FlowModel(
            config,
            self.dataset
        )

        self.pressure_model = PressureModel(
            config,
            self.dataset
        )

        # Initialize validator
        self.validator = Validator(config)

        # Create initial state
        self.state = self._create_initial_state()
        self.history = SimulationHistory()

    # ---------------------------------------------------------

    def _create_initial_state(self) -> WellState:
        """
        Creates the initial state of the simulator.
        """

        return WellState(
            time=0.0,
            flow=self.config.initial_flow,
            whp=self.config.initial_whp,
            flp=self.config.initial_flp,
            bhp=self.config.initial_bhp,
            choke=self.config.initial_choke,
        )

    # ---------------------------------------------------------

    def reset(self) -> WellState:
        """
        Reset simulator to initial conditions.
        """

        self.state = self._create_initial_state()
        self.history.clear()
        self.history.add(self.state)
        return self.state

    # ---------------------------------------------------------

    def step(self, new_choke: float) -> WellState:
        """
        Advance the simulator by one timestep.

        Parameters
        ----------
        new_choke : float
            Choke opening requested by the controller.

        Returns
        -------
        WellState
            Updated well state.
        """

        # Validate requested choke
        self.validator.validate_choke(new_choke)

        # Compute next flow
        new_flow = self.flow_model.next_flow(
            self.state,
            new_choke,
        )

        # Compute next pressures
        new_whp, new_flp, new_bhp = (
            self.pressure_model.next_pressures(
                self.state,
                new_choke,
            )
        )

        # Create next state
        next_state = WellState(
            time=self.state.time + self.config.time_step,
            flow=new_flow,
            whp=new_whp,
            flp=new_flp,
            bhp=new_bhp,
            choke=new_choke,
        )

        # Validate physical state
        self.validator.validate_state(next_state)

        # Update simulator
        self.state = next_state
        self.history.add(self.state)
        return self.state

    # ---------------------------------------------------------

    def current_state(self) -> WellState:
        """
        Return current simulator state.
        """

        return self.state

    def get_history(self):
        """
        Return simulation history.
        """
        return self.history