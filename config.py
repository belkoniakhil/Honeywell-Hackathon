"""
config.py
---------

Central configuration module for the Honeywell Autonomous
Production Choke Controller project.

This file contains ONLY configuration.

It must NEVER contain:

- Simulator logic
- Controller logic
- Mathematical equations
- Plotting code

Every module in the project should read configuration
from this file instead of hardcoding constants.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class SimulationConfig:
    """
    Immutable configuration for the entire simulation.

    All simulator behaviour should be configurable from here.
    """

    # ==========================================================
    # Simulation Settings
    # ==========================================================

    # Time between two simulation steps (seconds)
    time_step: float

    # Total simulation duration (seconds)
    simulation_time: float

    # Random seed (used when noise is enabled)
    random_seed: int

    # Enable / Disable sensor noise
    enable_noise: bool

    # ==========================================================
    # Choke Limits
    # ==========================================================

    # Minimum choke opening (%)
    min_choke: float

    # Maximum choke opening (%)
    max_choke: float

    # Maximum choke movement allowed per simulation step (%)
    max_choke_change: float

    # ==========================================================
    # Flow Limits
    # ==========================================================

    # Minimum oil production
    min_flow: float

    # Maximum oil production
    max_flow: float

    # ==========================================================
    # Pressure Limits
    # ==========================================================

    min_whp: float
    max_whp: float

    min_flp: float
    max_flp: float

    min_bhp: float
    max_bhp: float

    # ==========================================================
    # Dynamic Behaviour
    # ==========================================================

    # Response speed of flow
    flow_time_constant: float

    # Response speed of pressures
    pressure_time_constant: float

    # ==========================================================
    # Initial Well State
    # ==========================================================

    initial_flow: float

    initial_whp: float

    initial_flp: float

    initial_bhp: float

    initial_choke: float

    @classmethod
    def default(cls):
        """
        Creates the default configuration.

        NOTE:
        These values are temporary placeholders.

        Later we will calibrate them using
        the Honeywell sample dataset.
        """

        return cls(

            # Simulation
            time_step=1.0,
            simulation_time=300.0,
            random_seed=42,
            enable_noise=False,

            # Choke
            min_choke=0.0,
            max_choke=100.0,
            max_choke_change=5.0,

            # Flow
            min_flow=0.0,
            max_flow=200.0,

            # WHP
            min_whp=1000.0,
            max_whp=4000.0,

            # FLP
            min_flp=50.0,
            max_flp=500.0,

            # BHP
            min_bhp=1500.0,
            max_bhp=5000.0,

            # Dynamics
            flow_time_constant=8.0,
            pressure_time_constant=10.0,

            # Initial State
            initial_flow=100.0,
            initial_whp=2500.0,
            initial_flp=180.0,
            initial_bhp=3000.0,
            initial_choke=30.0,
        )